# write a Python program to show method overriding
# method overriding in python
class A:
    def show(self): 
        print("A calling..")


class B(A):
    def show(self):
        print("B calling")


b1 = B()
b1.show()