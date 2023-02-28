# programme to write table in python

a = input("Enter the number you want table of\n")

try:
    for i in range(1, 11):
        print(f"{int(a)} X {i} = {int(a)* i}")
except Exception as e:
    print("Error->Invalid input")
print("Some lines of code")
print("Code end")
