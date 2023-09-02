import sqlite3

conn = sqlite3.connect("concert_attendance.db")
cursor = conn.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS concerts
                  (id INTEGER PRIMARY KEY AUTOINCREMENT,
                   name TEXT,
                   date TEXT,
                   location TEXT)''')
conn.commit()

cursor.execute('''CREATE TABLE IF NOT EXISTS attendees
                  (id INTEGER PRIMARY KEY AUTOINCREMENT,
                   name TEXT,
                   ticket_number INTEGER,
                   concert_id INTEGER,
                   FOREIGN KEY (concert_id) REFERENCES concerts(id))''')
conn.commit()

def create_concert():
    name = input("Enter the concert name: ")
    date = input("Enter the concert date: ")
    location = input("Enter the concert location: ")

    cursor.execute("INSERT INTO concerts (name, date, location) VALUES (?, ?, ?)", (name, date, location))
    conn.commit()
    print("Concert created successfully!")

def display_concerts():
    cursor.execute("SELECT * FROM concerts")
    concerts = cursor.fetchall()

    if not concerts:
        print("No concerts found.")
    else:
        for concert in concerts:
            print(f"ID: {concert[0]}, Name: {concert[1]}, Date: {concert[2]}, Location: {concert[3]}")

def mark_attendance():
    display_concerts()
    concert_id = int(input("Enter the ID of the concert you want to mark attendance for: "))

    cursor.execute("SELECT * FROM attendees WHERE concert_id=?", (concert_id,))
    attendees = cursor.fetchall()

    if not attendees:
        print("No attendees found for this concert.")
    else:
        for attendee in attendees:
            print(f"ID: {attendee[0]}, Name: {attendee[1]}, Ticket Number: {attendee[2]}")

    attendee_name = input("Enter the name of the attendee: ")
    ticket_number = int(input("Enter the ticket number: "))

    cursor.execute("INSERT INTO attendees (name, ticket_number, concert_id) VALUES (?, ?, ?)", (attendee_name, ticket_number, concert_id))
    conn.commit()
    print("Attendance marked successfully!")

def main_menu():
    while True:
        print("\nConcert Attendance Management System")
        print("1. Create Concert")
        print("2. Display Concerts")
        print("3. Mark Attendance")
        print("4. Exit")
        choice = input("Enter your choice (1/2/3/4): ")

        if choice == '1':
            create_concert()
        elif choice == '2':
            display_concerts()
        elif choice == '3':
            mark_attendance()
        elif choice == '4':
            conn.close()
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main_menu()
