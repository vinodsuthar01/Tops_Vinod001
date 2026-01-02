# Write a Python program to read a name and age from the user and print a formatted output.
# 2) Write a Python program to read a string, an integer, and a float from the keyboard and display them.
def salary_():
    salary = (input("enter salary : "))
    x = float(salary)
    return x
name = input("enter name: ")
age = int(input("enter age: "))
salary = salary_()

print(f"Age of {name} is {age} and salary of {name} is {salary}")