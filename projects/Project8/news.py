import time
import requests
import pyttsx3
import datetime
Previous_Date = datetime.datetime.today() - datetime.timedelta(days=1)
Previous_Date = str(Previous_Date)
s = Previous_Date[0:10]


def speak(list1, list2):
    i = 0
    for i in range(i, len(list1)):
        print(list1[i])
        print()
        print(list2[i])
        print()
        print()
        engine = pyttsx3.init()
        engine.say(list1[i])
        engine.say(list2[i])
        engine.runAndWait()


# s = time.strftime("%Y-%m-%d")
print(s);
query = input("enter the type of news you want to see\n")
url = f"https://newsapi.org/v2/everything?q={query}&from={s}&sortBy=publishedAt&apiKey=7b0c876fc27f4a1ca878a1952a48a728"
response = requests.get(url)
helper = response.json()
helper = helper["articles"]
titleList = []
descriptionList = []
for title in helper:
    titleList.append(title["title"])
    descriptionList.append(title["description"])

# print(titleList)
# print(descriptionList)

speak(titleList, descriptionList)
