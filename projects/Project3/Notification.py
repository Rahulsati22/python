from notifypy import Notify
import time
while(True):
    notification = Notify()
    notification.title = "Drink Water"
    notification.message = "Take a break, drink water and chill"
    notification.icon=  "D:\python\projects\Project3\g.avif"
    notification.send()
    time.sleep(3600)