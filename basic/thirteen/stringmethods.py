a = "rahul sati is a good boy"

# method 1
print(len(a))

# method2
str1 = a.upper()
print(str1)


# method 3
str1 = a.lower()
print(str1)


# method 4
str1 = 'rahulssss'
# help to remove trailing characters
print(str1.rstrip("s"))  # output->rahul


# method 5
str1 = a.replace("rahul", "john")
print(str1)


# method 6
str1 = a.split(" ")
print(str1)
# output->['rahul', 'sati', 'is', 'a', 'good', 'boy']


# method 7
str1 = a.capitalize()
# first character ko uppercase and remaining character in lowercase
print(str1)


# method 8
str1 = a.center(50)
#             rahul sati is a good boy
print(str1)


# method 9
val = a.count("sati")
print(val)


# method 10
val = a.endswith("sati")
print(val)  # false
val = a.endswith("boy")
print(val)  # true


# method 11 -> find first occurrence
val = a.find("boy")
print(val)
val = a.find("b")
print(val)


# method 12
# -> simliar to find but give error if cannot find the string
val = a.index('boy')
print(val)


#method 13
val = a.isalnum();
print(val); #false
str = "12a";
print(str.isalnum()); # true



#method 14
val = a.isalpha();
print(val);  #false because it also has space character
str = "aaa";
print(str.isalpha()); #true because dont have space character



#method 15
val = a.islower();
print(val); #true because all the characters are in lower case



#method 16
val = a.isprintable();
print(val);
str = "hey\n";
val = str.isprintable();
print(val); #print false because \n is not printable



#method 17
str = "   ";
print(str.isspace()); # true because string is only a space



#method 18
print(a.istitle()); #false because first character is not capitalized
str = "Ayush"
print(str.istitle());


#method 19
print(a.swapcase()); #convert lowercase to uppercase and uppercase to lower case


#method 20
print(a.title()); #converts into title case (Rahul Sati Is A Good Boy)














'''
strings are immutable means we cannot change them inplace means we can change them but by making a new copy of them
'''
