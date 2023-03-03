a = 20
b = 30

print("a is greater than b") if (a > b) else print(
    "a is equals to b") if (a == b) else print("b is greater than a")

# not supported for multiple statements
c = True if (a > b) else False
print(c)
