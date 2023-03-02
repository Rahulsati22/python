def welcome():
    print("Welcome bro how are you")


# whenever we will import this file welcome function will automatically run
if (__name__ == "__main__"):
    welcome()


# whenever we print __name__ in the original file then it name will be main
# otherwise the __name__ will show the name of the file in which it is present from the other file
