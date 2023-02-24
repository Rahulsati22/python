#print number count to less than 100

count = int(input("Enter the number from where you want to start the count\n"));
while (True):
    print(count);
    count += 1;
    if (count % 100 == 0 or count > 100):
        break;