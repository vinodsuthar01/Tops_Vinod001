# 23) Write a Python program to search for a word in a string using re.search()
import re
st = "the sun rises in east"

k = re.search("sun",st)
print(k)