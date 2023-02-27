# old method starts
letter = "Hey my name is {} and I am from {}"
country = "India"
name = "Rahul"
print(letter.format(name, country))
# Hey my name is Harry and i am from India


letter = "Hey my name is {} and I am from {}"
country = "India"
name = "Rahul"
print(letter.format(country, name))
# Hey my name is India and i am from Rahul


letter = "Hey my name is {1} and I am from {0}"
country = "India"
name = "Rahul"
print(letter.format(country, name))
# Hey my name is Rahul and i am from India

# old method ends


# new method starts
name = "Rahul"
country = "India"
str = f"Hey my name is {name} and I am from {country}"
print(str)


price = 1.22222
str = f"The prize of this eraser is {price : .2f} dollars"
print(str)


print(
    f"We can user f strings like this - The name of the country is {{country}}")
# new methods ends
