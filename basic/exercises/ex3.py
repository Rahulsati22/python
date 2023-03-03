import pyttsx3
engine = pyttsx3.init()

print("Welcome to Kon bnega hazaarpati")
engine.say("Welcome to Kon bnega hazarpati")
engine.runAndWait()


i = 0
count = 0
key = ["A", "A", "B", "D", "D"]
list = ["Question number 1 Who is the father of the nation \n A Mahatma Gandhi \n B Rahul Sati \n C Akshay Kumar \n D.Amitabh Bachan",
        "Question number 2 Who is the president of India \n A Draupadi Murmu \n B Sunny Leone \n C Disha Patani \n D Ranee Mukherjee",
        "Question number 3 Who is the father of the constitution \n A Mahatma Gandhi \n B Br Ambedkar \n C Modiji \n D Yogi ji",
        "Question number 4 Giddha is the folk dance of\n A Goa \n B Bangkok \n C Australia \n D Punjab",
        "Question number 5 What is the capital of India\n A Goa \n B Bangkok \n C Australia \n D Delhi"]


while (i <= 4):
    print(list[i])
    engine.say(list[i])
    engine.runAndWait()
    ans = input("Enter your answer\n")
    if (ans == key[i]):
        engine.say("Correct answer")
        engine.runAndWait()
        count += 1
    else:
        engine.say("Sorry wrong answer you lost the game")
        str = "You won" + str(count * 10000) + "rupees"
        engine.say(str)
        engine.runAndWait()
        break
    i += 1


if (count == 5):
    engine.say("Hurrah you won the game")
    engine.say("You won 50,000 rupees")
    engine.runAndWait()
