# WEEK 8: Class Methods in Python

# In this session, we will explore class methods and how they can be used in our code.

# Step 1: Define a class for Student
class Student:
    def __init__(self, name, subject, test_result):
        self.name = name            # The student's name
        self.subject = subject      # The subject studied
        self.test_result = test_result  # The student's test result

    def pass_test(self):
        """Check if the student passed the test (score >= 75)."""
        if self.test_result >= 75:
            return True  # Student passed
        else:
            return False  # Student failed

# Step 2: Create instances of the Student class
student1 = Student("John", "Science", 78)
student2 = Student("Julie", "Math", 85)
student3 = Student("Matthew", "Sports", 65)

# Step 3: Use the pass_test method to check if each student passed
print(f"{student1.name} passed: {student1.pass_test()}")  # John passed: True
print(f"{student2.name} passed: {student2.pass_test()}")  # Julie passed: True
print(f"{student3.name} passed: {student3.pass_test()}")  # Matthew passed: False

# To identify which student failed
if not student3.pass_test():
    print(f"{student3.name} has failed their test.")

# Challenges:
# Challenge 1: Add an attribute for the student's age and modify the class accordingly.
# Challenge 2: Create a class method that calculates the average test result for a list of students.
# Challenge 3: Implement a class method that returns the details of the student as a formatted string.
# Challenge 4: Modify the class to allow adding more test results and checking for the best score.

# Example for Challenge 1:
class StudentWithAge:
    def __init__(self, name, subject, test_result, age):
        self.name = name
        self.subject = subject
        self.test_result = test_result
        self.age = age  # New attribute for age

    def pass_test(self):
        if self.test_result >= 75:
            return True
        else:
            return False

# Create instances of the new StudentWithAge class
student4 = StudentWithAge("Alice", "History", 90, 20)
print(f"{student4.name}, age {student4.age}, passed: {student4.pass_test()}")
