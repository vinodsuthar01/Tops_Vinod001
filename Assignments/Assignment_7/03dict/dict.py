# 13) Write a Python program to create a dictionary of 6 key-value pairs.
my_dict = {
    "name" : "Vinod",
    "sur_name" : "Suthar",
    "age" : 21,
    "village" : "Sarunda",
    "email" : "sutharv412@gmail.com",
    "phone" : 7877116879
}

# 14) Write a Python program to access values using keys from a dictionary.
for keys in my_dict.keys():
    print(my_dict.get(keys))

# 15) Write a Python program to update a value at a particular key in a dictionary.
my_dict.update({"name": "Ram"})

# 16) Write a Python program to separate keys and values from a dictionary using keys() and values() methods.
print(my_dict.keys(),"\n",my_dict.values())

# 17) Write a Python program to convert two lists into one dictionary using a for loop.
keys = ["name","age"]
values = ["Vinod",21]
my_dict1 = {}
for i in range(len(keys)):
    my_dict1[keys[i]] = values[i]
print(my_dict1)

# 18) Write a Python program to count how many times each character appears in a string.
st = "jjsjkslaljdlksjljf"
for ch in set(st):
    count = st.count(ch)
    print(ch,count)

