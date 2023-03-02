x = 4
print(f"the value of global x is {x}")
num = 20
print(f"the value of num is {num}")


def hello():
    # we want to change the value of num inside the hello function so how can we do that
    global num
    num = 5
    y = 10
    x = 5
    print(f"the value of local x is {x}")


hello()
print(f"the value of global x is {x}")
print(f"the value of num is {num}")
# print(f"the value of y is {y}") not possible because y is present inside the function and only have scope limited to the function and not global

# local variables are destroyed when the function gets return

# global keyword is used to change the global variable inside the function
