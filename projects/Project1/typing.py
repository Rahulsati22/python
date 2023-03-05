from time import *

list = ["my", "name", "is", "rahul", "sati", "decration", "intuition", "degree", "practical", "hero", "villain", "decoration", "statue", "air", "conditioner", "modile",
        "mobile", "psychology", "hero", "heroine", "comic", "penguin", "tigress", "alphanso", "numerical", "maths", "score", "scince", "history", "english", "child", "abuse"]

i = 0

print("*****Welcome to Rahul's typing test*****")
val = input(
    "Enter yes to start the test and enter exit anytime to exit the test\n")
if (val == 'yes'):
    i = 0
    score = 0
    error = 0
    timeInitial = round(time(), 2)
    while (i != len(list)):
        listWord = list[i]
        userWord = input(f"Enter this word : {list[i]}\n")
        if (userWord == 'exit'):
            break
        if (listWord == userWord):
            score += 1
        else:
            error += 1
        i += 1
    timeEnd = round(time(), 2)
    totalTime = timeEnd - timeInitial
    print(f"The number of errors are : {error}")
    print(f"Your speed is {round(score/totalTime,2) * 60} words/min")
