#question 1
#112307753

learners = []  # assign a list to store leaners
readings = []  # the list to store board readigns


def menu():
    print("\n Menu driven APP")
    print("1. Add Learner")
    print("2. Record Board Reading")
    print("3. Display Learners")
    print("4. Display Readings")
    print("5. Search Learner")
    print("6. Save Data")
    print("7. Exit")


def add_learner():
    learner_number = input("Enter learner number: ").strip()
    learner_name = input("Enter learner name: ").strip()
    programme = input("Enter course/programme: ").strip()

    if not learner_number or not learner_name or not programme:
        print("All fields are required!")
        return

    learners.append({"number": learner_number, "name": learner_name, "programme": programme})
    print("Learner is added!")


def record_reading():
    try:
        mark = int(input("Enter learner mark (1-100): "))
        if mark < 1 or mark > 100:
            print("Mark must be between 1 and 100.")
            return
        readings.append(mark)
        print("Reading recorded!")
    except ValueError:
        print("Please enter a valid numeric mark.")


def display_learners():
    if not learners:
        print("No learners found.")
    else:
        print("\n--- Learners ---")
        for learner in learners:
            print(f"Number: {learner['number']}, Name: {learner['name']}, Programme: {learner['programme']}")


def display_readings():
    if not readings:
        print("No readings recorded.")
    else:
        print("\n Readings")
        for idx, mark in enumerate(readings, start=1):
            print(f"Reading {idx}: {mark}")


def search_learner():
    search_number = input("Enter learner number to search: ").strip()
    for learner in learners:
        if learner["number"] == search_number:
            print(f"Found Learner: {learner['name']} ({learner['programme']})")
            return
    print("Learner not found.")


def save_data():
    try:
        with open("learners.txt", "w") as f:
            for learner in learners:
                f.write(f"{learner['number']},{learner['name']},{learner['programme']}\n")
        with open("readings.txt", "w") as f:
            for mark in readings:
                f.write(f"{mark}\n")
        print("Data saved successfully!")
    except Exception as e:
        print(f"Error saving data: {e}")


# the main loop for it to allways continue
while True:
    menu()
    choice = input("Enter option: ").strip()

    if choice == "1":
        add_learner()
    elif choice == "2":
        record_reading()
    elif choice == "3":
        display_learners()
    elif choice == "4":
        display_readings()
    elif choice == "5":
        search_learner()
    elif choice == "6":
        save_data()
    elif choice == "7":
        print("Exiting program...")
        break
    else:
        print("Invalid option. Please try again.")
