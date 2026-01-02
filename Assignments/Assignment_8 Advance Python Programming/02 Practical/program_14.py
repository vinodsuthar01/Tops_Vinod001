# 14) Write a Python program to show multilevel inheritance.
class A:
    def call_a(self):
        print("A calling")

class B(A):
    def call_b(self):
        print("B calling")

class C(B):
    def call_c(self):
        print("C calling")

c1 = C()
c1.call_a() #calling A
c1.call_b() #calling B
c1.call_c() #calling C