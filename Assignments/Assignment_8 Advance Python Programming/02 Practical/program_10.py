# 10) Write a Python program to print custom exceptions.
class AgeException(Exception):
    pass

try:
    age = int(input("enter age"))
    if age < 18:
        raise AgeException("not eligiable ") 
    else:
        print("eligiable")
except AgeException as e:
    print(e)