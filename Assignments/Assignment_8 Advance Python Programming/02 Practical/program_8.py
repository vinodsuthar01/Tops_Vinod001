# 8) Write a Python program to handle multiple exceptions (e.g., file not found, division by zero).
try:
    a = float(input("enter num 1: "))
    b = float(input("enter num 2: "))
    result = a/b

    with open("data.txt","r+") as f:
        f.write(str(result))
        print("result saved")
        
        f.seek(0)
        data = f.read()
        print(data)
except ZeroDivisionError:
    print("ZeroDivisionError")
except FileNotFoundError:
    print("FileNotFoundError")
except ValueError:
    print("value error")
except Exception as e:
    print("unknown error")