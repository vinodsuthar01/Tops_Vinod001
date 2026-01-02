# 13) Write a Python program to show single inheritance. 
# single inheritance
class A:
    def call_a(self):
        print("Class A calling....")


class B(A):
    def call_b(self):
        print("Class B calling....")


b1 = B()
b1.call_a() #use class A method
b1.call_b() #use class B method