# -*- coding: UTF-8 -*-

from fbchat import Client
from fbchat.models import *

#gets details
f=open("details.txt", "r")
details =f.read()
f.close()

detailsList = details.strip().split(",")
client = Client(detailsList[0], detailsList[1])


users = client.searchForUsers('<name of user>')
user = users[0]
print("User's ID: {}".format(user.uid))
print("User's name: {}".format(user.name))
print("User's profile picture url: {}".format(user.photo))
print("User's main url: {}".format(user.url))



print('Own id: {}'.format(client.uid))

client.send(Message(text='Hi me!'), thread_id=client.uid, thread_type=ThreadType.USER)

client.logout()
