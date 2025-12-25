# Write a Python program to create a tuple with multiple data types. 
my_tup = (34,"hello",True,45.5,56,"py")

# Write a Python program to concatenate two tuples.
tup1 = (34,"hello")
tup2 = ("python",56)
tup3 = tup1+tup2
print(tup3)

# Practical Examples: 7) Write a Python program to convert a list into a tuple. 
my_list = [1,3,4,5,6]
my_list = tuple(my_list)
print(my_list)


# 10) Write a Python program to access the value of the first index in a tuple.
print(my_tup[0])

# 11) Write a Python program to access values between index 1 and 5 in a tuple. 
print(my_tup[1:6])


# 12) Write a Python program to access the value from the last index in a tuple.
print(my_tup[-1])