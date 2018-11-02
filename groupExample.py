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

# Will send a message to the thread
client.send(Message(text='yeet2'), thread_id=thread_id, thread_type=thread_type)

client.logout()
