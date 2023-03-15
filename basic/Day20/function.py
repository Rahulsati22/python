def calculateMean(a, b):
    return (a*b)/(a+b)


# function to find which number is greater
def whichIsGreater(a, b):
    if (a > b):
        print("first number is greater than second number")

    elif (b > a):
        print("second number is greater than first number")

    else:
        print("first number is equals to second number")

# function to calculate mean


# a = 9;
# b = 8;
# ans = (a * b) / (a + b);
# print(ans);

# a = 10;
# b = 20;
# ans = (a * b) / (a+b);
# print(ans);


a = 20
b = 20
ans = calculateMean(a, b)
print(ans)
whichIsGreater(10, 50)
