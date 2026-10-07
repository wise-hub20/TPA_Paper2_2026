#QUESTIOPN 2
#112307753
learners = {}  #THE DICTIONARY


def add_learner():
    number = input("Enter learner number: ").strip()
    name = input("Enter learner name: ").strip()
    programme = input("Enter course/programme: ").strip()

    if not number or not name or not programme:
        print("All fields are required!")
        return

    if number in learners:
        print(" This learner already exists.")
        return

    learners[number] = {"name": name, "programme": programme, "marks": []}
    print("learner added!")


def record_mark():
    number = input("Enter learner number: ").strip()
    if number not in learners:
        print("learner not found.")
        return

    try:
        mark = int(input("Enter learner mark (1-100): "))
        if mark < 1 or mark > 100:
            print("Mark must be between 1 and 100.")
            return
        learners[number]["marks"].append(mark)
        print("Mark recorded successfully!")
    except ValueError:
        print("Please enter a valid numeric mark.")


def calculate_average(marks):
    if not marks:
        return 0
    return sum(marks) / len(marks)


def assign_status(avg):
    return "Pass" if avg >= 50 else "Fail"


def search_learner():
    number = input("Enter learner number to search: ").strip()
    if number in learners:
        learner = learners[number]
        avg = calculate_average(learner["marks"])
        status = assign_status(avg)
        print(f"\nlearner Found:")
        print(f"Number: {number}")
        print(f"Name: {learner['name']}")
        print(f"Programme: {learner['programme']}")
        print(f"Marks: {learner['marks']}")
        print(f"Average: {avg:.2f}")
        print(f"Status: {status}")
    else:
        print("learner not found.")


def display_all_learners():
    if not learners:
        print("No learners found.")
        return

    print("\n1Learners Table ")
    print(f"{'Number':<10}{'Name':<15}{'Programme':<15}{'Average':<10}{'Status':<10}")
    print("-" * 60)

    for number, learner in learners.items():
        avg = calculate_average(learner["marks"])
        status = assign_status(avg)
        print(f"{number:<10}{learner['name']:<15}{learner['programme']:<15}{avg:<10.2f}{status:<10}")


def menu():
    print("\nMenu driven APP")
    print("1. Add Learner")
    print("2. Record Mark")
    print("3. Search Learner")
    print("4. Display All Learners")
    print("5. Exit")


# Main loop
while True:
    menu()
    choice = input("Enter option: ").strip()

    if choice == "1":
        add_learner()
    elif choice == "2":
        record_mark()
    elif choice == "3":
        search_learner()
    elif choice == "4":
        display_all_learners()
    elif choice == "5":
        print("Exiting program...")
        break
    else:
        print("Please try again.")
