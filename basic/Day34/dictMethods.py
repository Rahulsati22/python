id = {
    1: "rahul",
    2: "ayush",
    3: "akshay",
    4: "shakal",
    5: "hritik"
}
id2 = {
    6: "shahrukh",
    7: "ranbeer"
}

# method 1
id.update(id2)
print(id)

# method 2
id2.clear()
print(id2)

# method 3
print(id.pop(1))  # ->it will provide the value of the key we are popping
print(id)

# method 4
# ->it will remove the last element of the dictionary and return the whole key-value pair
print(id.popitem())
print(id)


# method 5
del id2  # it will delete the whole dictionary means dictionary does not exist
# print(id2);  this will give an error


# method 6
del id[2]
print(id)
