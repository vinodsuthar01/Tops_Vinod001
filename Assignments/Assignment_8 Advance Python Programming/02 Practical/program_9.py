# 9) Write a Python program to handle file exceptions and use the finally block for closing the file.
f = None
file_name = input("enter file name : ")
try:
    
    f = open(f"{file_name}","r")
    data = f.read()
    print(data)
except FileNotFoundError:
    print("file not found")
finally:
    if f:
        f.close()

