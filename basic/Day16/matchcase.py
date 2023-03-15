x = int(input("Enter your number between 1-5 below\n"));

match x:
    case 1 :
        print("The value of number is 1");
    case 2 :
        print("The value of number is 2");
    case 3 :
        print("The value of number is 3");
    case 4 : 
        print("The value of number is 4");
    case 5 : 
        print("The value of number is 5");
    case _:
        if(x <= 0):
            print("The number should be greater than zero");
        else:
            print("The number should be less than 5");

