"""Beginner Python practice."""
def calculate_average(numbers):
    return sum(numbers) / len(numbers) if numbers else 0

def main():
    student = {"name": "Anushka", "course": "Python",
               "topics": ["variables", "loops", "functions", "data structures"]}
    print("Student:", student["name"])
    for topic in student["topics"]:
        print("-", topic)
    print("Average:", calculate_average([80, 90, 85]))

if __name__ == "__main__":
    main()
