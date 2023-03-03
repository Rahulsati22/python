
try:
    a = [1, 2, 4]
    num = int(input("Enter the index you want to access\n"))
    print(a[num])
except ValueError as err:
    print("Enter the integer")
except IndexError as err:
    print("Enter the index in range")
    
    
print("some important code")