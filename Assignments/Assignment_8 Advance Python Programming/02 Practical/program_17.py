# 17) Write a Python program to show hybrid inheritance.
class A:
    def call_a(self):
        print("A calling")

class B(A):
    def call_b(self):
        print("B calling")

class C(A):
    def call_c(self):
        print("C calling")

class D(B,C):
    def call_d(self):
        print("D calling")

b1 = B()
b1.call_a()
b1.call_b()

c1 = C()
c1.call_a()
c1.call_c()

d1 = D()
d1.call_a()
d1.call_b()
d1.call_c()
d1.call_d()

