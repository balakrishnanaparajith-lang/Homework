#Question 1. Create a Student class that stores student details and attendance records using dictionaries.
# Use functions, loops, conditional statements, and sets to manage attendance percentage and check exam eligibility.

def student():
    dictionary = {"bob":87,
            "billy":67,
            "rob":99}
    for name, attendance in dictionary.items():
        if attendance < 70:
            print(f"{name} is NOT eligible for exam")
        elif attendance < 90:
            print(f"{name} is eligible but needs improvement")
        else:
             print(f"{name} is FULLY eligible for exam")
student()



