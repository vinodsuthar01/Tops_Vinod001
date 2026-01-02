# 7) Write a Python program to handle exceptions in a calculator.

def add(a,b):
    sum = a+b
    print(f"Sum : {sum}")

def sub(a,b):
    sub = a-b
    print(f"Sub : {sub}")

def divi(a,b):

    try:
        div = a/b
        print(f"div : {div}")
    except ZeroDivisionError as e:
        print(e)


def multi(a,b):
    mul = a*b
    print(f"multi : {mul}")

def modulo(a,b):
    mod = a%b
    print(f"mod : {mod}")

def power(a,b):
    pow = a**b
    print(f"Power : {pow}")


def calc():    
    
    try:
        a = float(input("enter num: "))
        c = (input("enter +|-|*|/: "))
        b = float(input("enter num: "))
        if c == "+":
            add(a,b)
        elif c == "-":
            sub(a,b)
        elif c == "*":
            multi(a,b)
        elif c == "/":
            divi(a,b)
        elif c == "%":
            modulo(a,b)
        elif c == "**":
            power(a,b)
        else:
            print("invalid choice....")
    except ValueError as e:
        print(e)
    
    

choice = "y"
while choice == "y":
    if choice == "n":
        break
    calc()
    choice = input("enter choice : ")