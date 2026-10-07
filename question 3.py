#questuion 3
#112307753


class Learner:
    def __init__(self, number, name, programme, marks=None):
        self.number = number
        self.name = name
        self.programme = programme
        self.marks = marks if marks is not None else []

    def average(self):
        if not self.marks:
            return 0
        return sum(self.marks) / len(self.marks)

    def status(self):
        return "Pass" if self.average() >= 50 else "Fail"

    def display(self):
        print(f"Number: {self.number}")
        print(f"Name: {self.name}")
        print(f"Programme: {self.programme}")
        print(f"Marks: {self.marks}")
        print(f"Average: {self.average():.2f}")
        print(f"Status: {self.status()}")


# list or collection of the learners
learners = []


def add_learner():
    number = input("Enter learner number: ").strip()
    name = input("Enter learner name: ").strip()
    programme = input("Enter course/programme: ").strip()

    if not number or not name or not programme:
        print("All fields are required!")
        return

    # it just prevent duplicate learner numbers mkaing them not to me duplicate
    for l in learners:
        if l.number == number:
            print("the learner already exists.")
            return

    learner = Learner(number, name, programme)
    learners.append(learner)
    print("learner added!")


def record_mark():
    number = input("Enter learner number: ").strip()
    for learner in learners:
        if learner.number == number:
            try:
                mark = int(input("Enter learner mark (1-100): "))
                if mark < 1 or mark > 100:
                    print("Mark must be between 1 and 100.")
                    return
                learner.marks.append(mark)
                print("Mark recorded!")
            except ValueError:
                print("Please just enter a valid numeric mark.")
            return
    print("learner not found.")


def search_learner():
    number = input("Enter learner number to search: ").strip()
    for learner in learners:
        if learner.number == number:
            print("\nLearner Found:")
            learner.display()
            return
    print("learner not found.")


def display_all_learners():
    if not learners:
        print("No learners found.")
        return

    print("\nLearners Table")
    print(f"{'Number':<10}{'Name':<15}{'Programme':<15}{'Average':<10}{'Status':<10}")
    print("-" * 60)

    for learner in learners:
        print(f"{learner.number:<10}{learner.name:<15}{learner.programme:<15}{learner.average():<10.2f}{learner.status():<10}")


def menu():
    print("\nMenu driven APP")
    print("1. Add learner")
    print("2. Record Mark")
    print("3. Search learner")
    print("4. Display All learners")
    print("5. Exit")


# Create at least three learner objects
learners.append(Learner("001", "mokgosi", "Computer Science", [78, 85, 90]))
learners.append(Learner("002", "tshepo", "Mathematics", [45, 50, 55]))
learners.append(Learner("003", "kea", "Robotics", [30, 40, 35]))


# this is the main loop it maskes sure it reapets the things
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
