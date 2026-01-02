#  6) Write a Python program to check the current position of the file cursor using tell().
with open("demo.txt","r") as f:
    cur = f.tell()
    print(f"cursor at the start {cur}")
    data = f.read()
    cur = f.tell()
    print(f"cursor at the end {cur}")