# 18) Write a Python program to demonstrate the use of super() in inheritance.
class A:
    def __init__(self):
        print("A calling")

class B(A):
    def __init__(self):
        super().__init__()


b1 = B()
