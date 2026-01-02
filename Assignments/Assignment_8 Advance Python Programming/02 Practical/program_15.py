# 15) Write a Python program to show multiple inheritance. 
# multiple inheritance
class A:
    def call_a(self):
        print("A calling...")

class B:
    def call_b(self):
        print("B calling...")

class C(A,B):
    def call_c(self):
        print("C calling...")



# create class C object and using A and B both method
c1 = C()
c1.call_a()
c1.call_b()