# 24) Write a Python program to match a word in a string using re.match().
import re

st = input("Enter Str: ")
start_from = input("Enter with Start: ")

k = re.match(start_from,st)
if k:
    print("str start with this word")
else:
    print("str not start with this word")