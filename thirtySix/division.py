a = input("Enter the value of first number\n")
b = input("Enter the value of second number\n")

try:
    print(f"{a}/{b} = {int(a)/int(b)}")
except Exception as e:
    print("Enter the correct value for a and b")


print("Some code");