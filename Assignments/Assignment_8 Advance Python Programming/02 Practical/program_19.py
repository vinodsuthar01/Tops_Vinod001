# 19) Write a Python program to show method overloading.
# method overloading in python does not support directely but using *args can be do this
class A:
    def sum_of(self,*a):
        self.a  = a
        print(sum(a))

a1 = A()
a1.sum_of(1,2,3,4,5,6,7)
a1.sum_of(1,2,3,4)
a1.sum_of(1,2)


