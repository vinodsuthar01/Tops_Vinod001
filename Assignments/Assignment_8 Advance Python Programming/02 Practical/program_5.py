# 5) Write a Python program to read a file and print the data on the console.
with open("demo.txt","r") as f:
    data = f.read()
    print(data)