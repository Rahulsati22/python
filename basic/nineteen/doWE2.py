#programme to print number while it is greater than 0
count = int(input("Enter the number from where you want to start the count\n"));
while(True):
    print(count);
    count = int(input("Enter the number from where you want to start the count\n"));
    if(count <= 0):
        break;