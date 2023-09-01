class User:
    def __init__(self, name, age, gender, hobbies):
        self.name = name
        self.age = age
        self.gender = gender
        self.hobbies = hobbies

def calculate_match_score(user1, user2):
    # Define your matching criteria here. This is just a simple example.
    score = 0

    if user1.age == user2.age:
        score += 10

    if user1.gender != user2.gender:
        score += 20

    common_hobbies = set(user1.hobbies) & set(user2.hobbies)
    score += len(common_hobbies) * 5

    return score

def main():
    users = []

    while True:
        name = input("Enter your name (or 'exit' to quit): ")
        if name.lower() == 'exit':
            break

        age = int(input("Enter your age: "))
        gender = input("Enter your gender (male/female): ")
        hobbies = input("Enter your hobbies (comma-separated): ").split(',')

        user = User(name, age, gender, hobbies)
        users.append(user)

    print("\nMatching Results:")
    for i, user1 in enumerate(users):
        for j, user2 in enumerate(users):
            if i != j:
                match_score = calculate_match_score(user1, user2)
                print(f"{user1.name} and {user2.name}: Match Score {match_score}")

if __name__ == "__main__":
    main()
