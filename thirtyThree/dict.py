dict = {
    "rahul": "human",
    "laptop": "machine",
    "dog": "animal",
}

marks = {
    "rahul sati": "100",
    "rahul bisht": "100",
    "ayush sati": "100",
    "ayush sati": "200",
}

id = {
    1: "rahul sati",
    2: "akshay sharma",
    3: "ayush sati"
}

print(marks["rahul sati"], marks["rahul bisht"], marks["ayush sati"])
print(dict["rahul"], dict["laptop"], dict["dog"])

# what is the difference between these two
# if we try to access a key which is not present in dictionary first method will give an error ehile second will not give an error
print(id[1], id[2], id[3])
print(id.get(1), id.get(2), id.get(3))

# iterating using for loop
for i in marks.values():
    print(i)

for i in marks.keys():
    print(i + "->" + marks[i])


# using f string with it
for i in id.keys():
    print(
        f"The id of the employee is {i} and the name of the employee is {id[i]}")


print(id.items())
'''
dictionaries are ordered collection of data items. They store multiple items in a single variable. Dictionary items are key-value pairs that are separated by commas and enclosed within curly brackets{}; 
'''
