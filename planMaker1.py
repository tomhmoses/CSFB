# -*- coding: UTF-8 -*-

from fbchat import Client
from fbchat.models import *

#gets details
f=open("details.txt", "r")
details =f.read()
f.close()

detailsList = details.strip().split(",")
client = Client(detailsList[0], detailsList[1])



thread_id = detailsList[2]
thread_type = ThreadType.GROUP

startingLocationString = "Starbucks ⇨ "

#creates a plan object

newPlan = Plan(1541235600,"08:45 meet", startingLocationString + "Some Lecture Theatre")


# Will send the plan
client.createPlan(newPlan, thread_id=thread_id)

client.logout()
