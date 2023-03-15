# today we will study about regular expressions in python
import re
pattern = r"[A-Z]+yclone"
text = "hey my name is rahul sati how are you and what is your name Cyclone cyclone Byclone"
# this stops on first match
matching = re.search(pattern, text)
print(matching)

# this will find all the matches
matching = re.finditer(pattern, text)
for match in matching:
    print(match)
    # from where the string starts and where it is ending
    print(match.span())
    # this is a tupple
    print(type(match.span()))
    # another way to find and print the pattern
    print(text[match.span()[0]: match.span()[1]])
