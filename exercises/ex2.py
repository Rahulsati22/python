from time import time, ctime
import pyttsx3
t = time()
val = ctime(t)
hour = int(val[11:13])
engine = pyttsx3.init()

if (hour >= 0 and hour < 12):
    engine.say("Good morning sir")
    engine.runAndWait()

elif (hour >= 12 and hour < 17):
    engine.say("Good afternoon sir")
    engine.runAndWait()

elif (hour >= 17 and hour <= 23):
    engine.say("Good evening sir")
    engine.runAndWait()
