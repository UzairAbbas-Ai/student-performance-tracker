
class Student:
    def __init__(self, name, scores):
        self.name = name
        self.scores = scores
    def calculate_average(self):
        return sum(self.scores) / len(self.scores)
    def is_passing(self, passing_score=40):
        return all(score >= passing_score for score in self.scores)
class PerformanceTracker:
    def __init__(self):
        self.students = {}
    def add_student(self, name, scores):
        if name in self.students:
            print(f"Student {name} already exists. Updating scores.")
        self.students[name] = Student(name, scores)
    def calculate_class_average(self):
        if not self.students:
            print("No students in the tracker.")
            return 0
        total_average = sum(student.calculate_average() for student in self.students.values())
        return total_average / len(self.students)
    def display_student_performance(self):
        if not self.students:
            print("No students to display.")
            return
        print("\nStudent Performance:")
        print("-" * 40)
        for name, student in self.students.items():
            average = student.calculate_average()
            status = "Passing" if student.is_passing() else "Needs Improvement"
            print(f"Name: {name}, Average: {average:.2f}, Status: {status}")
        print("-" * 40)
def main():
    tracker = PerformanceTracker()
    while True:
        print("\n--- Student Performance Tracker ---")
        print("1. Add Student")
        print("2. Display All Performance")
        print("3. Calculate Class Average")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter student name: ")
            scores = []

            try:
                for subject in ["Math", "Science", "English"]:
                    score = int(input(f"Enter {subject} score: "))
                    if score < 0 or score > 100:
                        raise ValueError("Score must be between 0 and 100.")
                    scores.append(score)
                tracker.add_student(name, scores)
            except ValueError as e:
                print(f"Invalid input: {e}")

        elif choice == "2":
            tracker.display_student_performance()

        elif choice == "3":
            class_avg = tracker.calculate_class_average()
            print(f"\nClass Average: {class_avg:.2f}")

        elif choice == "4":
            print("Exiting... Goodbye!")
            break

        else:
            print("Invalid choice. Please select a valid option.")


if __name__ == "__main__":
    main()
