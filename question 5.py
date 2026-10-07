#question 5
#112307753
import csv

class Learner:
    def __init__(self, number, name, programme, marks=None):
        self.number = number
        self.name = name
        self.programme = programme
        self.marks = marks if marks is not None else []

    def average(self):
        return sum(self.marks) / len(self.marks) if self.marks else 0

    def status(self):
        return "Pass" if self.average() >= 50 else "Fail"

    def display(self):
        print(f"Number: {self.number}")
        print(f"Name: {self.name}")
        print(f"Programme: {self.programme}")
        print(f"Marks: {self.marks}")
        print(f"Average: {self.average():.2f}")
        print(f"Status: {self.status()}")

#collection of data
learners = []

#assignig functions
def add_learner():
    number = input("Enter learner number: ").strip()
    name = input("Enter learner name: ").strip()
    programme = input("Enter course/programme: ").strip()

    if not number or not name or not programme:
        print("All fields are required!")
        return

    for l in learners:
        if l.number == number:
            print("Learner already exists.")
            return

    learner = Learner(number, name, programme)
    learners.append(learner)
    print("Learner added!")

def record_mark():
    number = input("Enter learner number: ").strip()
    for learner in learners:
        if learner.number == number:
            try:
                mark = int(input("Enter learner mark (1-100): "))
                if 1 <= mark <= 100:
                    learner.marks.append(mark)
                    print("Mark recorded!")
                else:
                    print("Mark must be between 1 and 100.")
            except ValueError:
                print("Please enter a valid numeric mark.")
            return
    print("Learner not found.")

def search_learner():
    number = input("Enter learner number to search: ").strip()
    for learner in learners:
        if learner.number == number:
            print("\nLearner Found:")
            learner.display()
            return
    print("Learner not found.")

def display_all_learners():
    if not learners:
        print("No learners found.")
        return

    print("\nLearners Table")
    print(f"{'Number':<10}{'Name':<15}{'Programme':<15}{'Average':<10}{'Status':<10}")
    print("-" * 60)
    for learner in learners:
        print(f"{learner.number:<10}{learner.name:<15}{learner.programme:<15}{learner.average():<10.2f}{learner.status():<10}")

def save_learners(filename="learners.csv"):
    with open(filename, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["number", "name", "programme", "marks"])
        for l in learners:
            writer.writerow([l.number, l.name, l.programme, ",".join(map(str, l.marks))])
    print("Learners saved to file.")

def load_learners(filename="learners.csv"):
    learners.clear()
    try:
        with open(filename, "r") as f:
            reader = csv.DictReader(f)
            for row in reader:
                marks = [int(m) for m in row["marks"].split(",")] if row["marks"] else []
                learners.append(Learner(row["number"], row["name"], row["programme"], marks))
        print("Learners loaded from file.")
    except FileNotFoundError:
        print("No saved learners found.")


def menu():
    print("\nMenu driven APP")
    print("1. Add learner")
    print("2. Record Mark")
    print("3. Search learner")
    print("4. Display All learners")
    print("5. Save learners")
    print("6. Load learners")
    print("7. Exit")

# Preloaded learners for csv file tgest
learners.append(Learner("001", "mokgosi", "Computer Science", [78, 85, 90]))
learners.append(Learner("002", "tshepo", "Mathematics", [45, 50, 55]))
learners.append(Learner("003", "kea", "Robotics", [30, 40, 35]))

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
        save_learners()
    elif choice == "6":
        load_learners()
    elif choice == "7":
        print("Exiting program...")
        break
    else:
        print("Please try again.")
