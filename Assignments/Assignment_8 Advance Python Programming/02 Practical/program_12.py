# 12) Write a Python program to demonstrate the use of local and global variables in a class.
# Global variable
a = 20

class Student:
    b = 10   # Class variable

    def show(self):
        c = 5   # Local variable
        print("Global variable a:", a)
        print("Class variable b:", self.b)
        print("Local variable c:", c)

# Object creation
s1 = Student()
s1.show()

print("Accessing global variable outside class:", a)
