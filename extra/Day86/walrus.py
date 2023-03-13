a = True
# this will give error
# print(a=False)

# now using walrus operator we can achieve this
# walrus -> assign value to variables as a part of a larger expression
print(a := False)

# another example
list = [1, 2, 3, 4, 5]
while (n := len(list)) > 0:
    print(list.pop())

# another example
val = False
print(val)
print(val := True)


# without walrus operator
while True:
    fruit = input("enter the fruit you like\n")
    if (fruit == "quit"):
        break
    else:
        print(fruit)

# with walrus operator
while (fruit := input("enter the fruit you like\n")) != "quit":
    print(fruit)
