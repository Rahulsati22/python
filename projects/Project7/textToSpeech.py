import win32com.client
speaker = win32com.client.Dispatch("SAPI.SpVoice")
list = ["rahul", "ayush", "akshay"]
for i in list:
    speaker.Speak(i)