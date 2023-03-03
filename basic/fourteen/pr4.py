val = int(input("Enter your number\n"))
if (val > 0):
    if (val > 0 and val < 20):
        print("The number is between 1-20")
    else:
        print("The number is greater than or equal to 20")

elif (val == 0):
    print("The value of the number is zero")

else:
    print("Thev value of the number is less than zero")
