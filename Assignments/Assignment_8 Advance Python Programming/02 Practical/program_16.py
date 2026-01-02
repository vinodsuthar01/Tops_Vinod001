# 16) Write a Python program to show hierarchical inheritance.
# hierarchical inheritance
class A:
    def call_a(self):
        print("A calling....")

class B(A):
    def call_b(self):
        print("B calling....")

class C(A):
    def call_c(self):
        print("C calling....")

# created B class ob and using A method
b1 = B()
b1.call_a()
b1.call_b()
# created C class ob and using A method
c1 = C()
c1.call_a()
c1.call_c()
