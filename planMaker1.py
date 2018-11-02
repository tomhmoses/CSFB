# -*- coding: UTF-8 -*-

from fbchat import Client
from fbchat.models import *

#gets details
f=open("details.txt", "r")
details =f.read()
f.close()

detailsList = details.strip().split(",")
client = Client(detailsList[0], detailsList[1])



thread_id = '1829194537197296'
thread_type = ThreadType.GROUP

#creates a plan object

newPlan = Plan(1541235600,"test plan name", "tom's laptop")


# Will send the plan
client.createPlan(newPlan, thread_id=thread_id)

client.logout()
