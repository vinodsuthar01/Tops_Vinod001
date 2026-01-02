# Write a Python program to open a file in write mode, write some text, and then close it. 
# 3) Write a Python program to create a file and write a string into it.

with open("demo.txt","w") as f:
    f.write("hello, python")
    print("file created...")