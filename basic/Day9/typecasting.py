a = "1";
b = "2";


# output will be 12 as we are concatenating two string
print(a + b);


a = 1;
b = 2;

#output will be 3 as we are adding two numbers
print(a + b);


'''
#! type conversion
#*conversion of one datatype into another data type is known as type conversion
#*python supports the following type conversions

#these functions will (try) to convert one datatype into another
int(), float(), str(), ord(), hex(), oct(), tuple(), set(), list(), dict(), etc.


#!two types of type casting
1) implicit typecasting --> done by the python itself
2) explicit typecasting --> done by the programmer using above mentioned functions
'''


c = int("1");
print(c);

# d = int("harry");-->invalid
# print(d);-->invalid

num1 = "1";
num2 = "2";
print(num1 + num2) #ans=12

print(int(num1) + int(num2)); # ans = 3



num1 = 1.5
num2 =1 
#here num1 is higher data type and num2 is lower datatype so when addition will happen the python will convert the lower data type to higher data type to avoid data loss so the final answer will be a float 
print(num1 + num2);