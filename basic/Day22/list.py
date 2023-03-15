# this is a list
marks = [2, 5, 6]

# printing the whole list
print(marks)


# printing the list elements
print(type(list))
print(marks[0])
print(marks[1])
print(marks[2])

# adding elements in the list
marks.append(10)
marks.append(20)

# printing the marks again
print(marks)
print(len(marks))
# print(marks[10])-->it will give us error

# printing element using negative indexing
print(marks[-3])


# to check whether an element is present in list or not
if 18 in marks:
    print("Yes")
else:
    print("No")


# applying same thing in string

if "hul" in "rahul":
    print("Yes")
else:
    print("No")


# .printing all elements of list
print(marks)
print(marks[:])
print(marks[0:])
print(marks[:len(marks)])


# not printing all the elements
print(marks[:3])


# using jump index
print(marks[::2])


'''
ek nam ke andr bhut sari values ko rkh diya
list are ordered collection of data items
list items are separated by commas and are closed by square brackets
list are changable
'''
