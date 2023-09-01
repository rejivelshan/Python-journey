import sqlite3


class Hotel:
    def __init__(self, name, capacity):
        self.name = name
        self.capacity = capacity
        self.conn = sqlite3.connect('hotel.db')
        self.create_tables()

    def create_tables(self):
        cursor = self.conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS rooms (
                room_number TEXT PRIMARY KEY,
                guest_name TEXT
            )
        ''')
        self.conn.commit()

    def display_available_rooms(self):
        cursor = self.conn.cursor()
        cursor.execute('SELECT room_number FROM rooms WHERE guest_name IS NULL')
        available_rooms = [row[0] for row in cursor.fetchall()]
        print(f"Available rooms in {self.name}: {', '.join(available_rooms)}")

    def book_room(self, room_number, guest_name):
        cursor = self.conn.cursor()
        cursor.execute('SELECT guest_name FROM rooms WHERE room_number = ?', (room_number,))
        result = cursor.fetchone()

        if result and result[0] is not None:
            print(f"Room {room_number} is not available.")
        else:
            cursor.execute('UPDATE rooms SET guest_name = ? WHERE room_number = ?', (guest_name, room_number))
            self.conn.commit()
            print(f"Room {room_number} has been booked by {guest_name}.")

    def check_out(self, room_number):
        cursor = self.conn.cursor()
        cursor.execute('SELECT guest_name FROM rooms WHERE room_number = ?', (room_number,))
        result = cursor.fetchone()

        if result and result[0]:
            guest_name = result[0]
            cursor.execute('UPDATE rooms SET guest_name = NULL WHERE room_number = ?', (room_number,))
            self.conn.commit()
            print(f"{guest_name} has checked out of Room {room_number}.")
        else:
            print(f"Room {room_number} is not occupied.")

    def show_guests(self):
        cursor = self.conn.cursor()
        cursor.execute('SELECT room_number, guest_name FROM rooms WHERE guest_name IS NOT NULL')
        guests = cursor.fetchall()
        for room, guest in guests:
            print(f"Room {room}: {guest}")


def main():
    hotel_name = "Sample Hotel"
    total_rooms = 10
    hotel = Hotel(hotel_name, total_rooms)

    while True:
        print("\nHotel Booking System")
        print("1. Display available rooms")
        print("2. Book a room")
        print("3. Check-out")
        print("4. Show guests")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            hotel.display_available_rooms()
        elif choice == "2":
            room_number = input("Enter the room number to book: ")
            guest_name = input("Enter the guest name: ")
            hotel.book_room(room_number, guest_name)
        elif choice == "3":
            room_number = input("Enter the room number to check-out: ")
            hotel.check_out(room_number)
        elif choice == "4":
            hotel.show_guests()
        elif choice == "5":
            hotel.conn.close()
            print("Exiting the Hotel Booking System. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")


if __name__ == "__main__":
    main()
