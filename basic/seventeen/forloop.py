
str = "Rahul sati is a good boy"

# programme 1 print string in one line
for i in str:
    print(i, end='')
    if (i == "R"):
        print("This is the first character of my name")

print()

# programme 2 print string reverse
for i in str[::-1]:
    print(i, end='')

print()

# programme 3 print elements of a list
list = ["Rahul", "Ayush", "Akshay", "Shahrukh"]
for i in list:
    for j in i:
        print(j, end='->')

print()

# programme 4 -> to print in a range
for i in range(1, 5):
    print(i, end=' ')

print()

# programme 5
for i in range(5):
    print(i, end=' ')

print()

# print the table of 2
x = 1
for i in range(2, 21, 2):
    print(i, end=' ')
