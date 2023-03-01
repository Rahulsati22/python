a = input("Enter any value from 1 to 10\n")

# agar ye condition satisfy na hui to isi point pe ek error aa jaega
# by using raise keyword we can raise the custom error

if (a != 'quit'):
    if (int(a) < 1 or int(a) > 10):
        raise ValueError(
            "The value should be from 1 to 10 please enter a correct value")


print("Some lines of code")
