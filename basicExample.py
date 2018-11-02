# -*- coding: UTF-8 -*-

#from fbchat import Client
#from fbchat.models import *

#gets details
f=open("details.txt", "r")
details =f.read()
f.close()

print details.strip().split(",")


client = Client(details[0], details[1])

print('Own id: {}'.format(client.uid))

client.send(Message(text='Hi me!'), thread_id=client.uid, thread_type=ThreadType.USER)

client.logout()