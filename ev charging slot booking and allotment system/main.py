class ChargingStation:
    def __init__(self, name, capacity):
        self.name = name
        self.capacity = capacity
        self.slots = {str(i): None for i in range(1, capacity + 1)}


class UserDatabase:
    def __init__(self):
        self.users = {}

    def register_user(self, username, password):
        if username not in self.users:
            self.users[username] = password
            print("Registration successful.")
        else:
            print("Username already exists. Please choose a different username.")

    def login_user(self, username, password):
        if username in self.users and self.users[username] == password:
            return True
        else:
            return False


def main():
    charging_station = ChargingStation("Sample Charging Station", capacity=10)
    user_db = UserDatabase()
    current_user = None

    while True:
        print("\nEV Charging Station Slot Booking System")
        print("1. Register")
        print("2. Log In")
        print("3. View Available Slots")
        print("4. Book a Slot")
        print("5. Log Out")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            username = input("Enter a username: ")
            password = input("Enter a password: ")
            user_db.register_user(username, password)
        elif choice == "2":
            if current_user:
                print("You are already logged in.")
            else:
                username = input("Enter your username: ")
                password = input("Enter your password: ")
                if user_db.login_user(username, password):
                    current_user = username
                    print(f"Logged in as {current_user}.")
                else:
                    print("Invalid username or password.")
        elif choice == "3":
            print(f"Available slots at {charging_station.name}:")
            available_slots = [slot for slot, user in charging_station.slots.items() if user is None]
            print(", ".join(available_slots))
        elif choice == "4":
            if not current_user:
                print("Please log in first.")
            else:
                slot_number = input("Enter the slot number to book: ")
                if slot_number in charging_station.slots and charging_station.slots[slot_number] is None:
                    charging_station.slots[slot_number] = current_user
                    print(f"Slot {slot_number} has been booked by {current_user}.")
                else:
                    print(f"Slot {slot_number} is not available.")
        elif choice == "5":
            current_user = None
            print("Logged out.")
        elif choice == "6":
            print("Exiting the EV Charging Station Slot Booking System. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")


if __name__ == "__main__":
    main()
