# -*- coding: UTF-8 -*-

from fbchat import Client
from fbchat.models import *
from getNextTimeTableEvent import getNextEventDetails
import datetime
import time


def postPlanToGroup(newPlan):
    f=open("facebookDetails.txt", "r")
    details =f.read()
    f.close()

    detailsList = details.strip().split(",")
    client = Client(detailsList[0], detailsList[1])

    thread_id = detailsList[2]
    thread_type = ThreadType.GROUP

    # Will send the plan
    client.createPlan(newPlan, thread_id=thread_id)
    print "made plan"
    client.logout()

def postTestMessage():
    f=open("facebookDetails.txt", "r")
    details =f.read()
    f.close()

    detailsList = details.strip().split(",")

    client = Client(detailsList[0], detailsList[1])

    print('Own id: {}'.format(client.uid))

    client.send(Message(text='Bot started and ready to send a plan to: ' + str(detailsList[2])), thread_id=client.uid, thread_type=ThreadType.USER)

    client.logout()






def getWalkingTime(location):
    locationTimeArray = [["Physics West", 10],
                        ["Gisbert Kapp", 15],
                        ["Mech Eng", 5],
                        ["University House", 10],
                        ["Aston Webb Main LT", 10]
                        ]
    for each in locationTimeArray:
        if each[0] in location:
            return each[1]
    #returns 0 if time is unknown
    return 0


def stringTimeToDatetime(start):
    startTime = datetime.datetime(int(start[0:4]),int(start[5:7]),int(start[8:10]),int(start[11:13]),int(start[14:16]))
    return startTime

def getTimeToMeet(start,location):
    waitTime = 5
    walkingTime = getWalkingTime(location)
    if walkingTime == 0:
        return "UNKNOWN"
    mins = waitTime + walkingTime
    startTime = stringTimeToDatetime(start)
    minsDelta = datetime.timedelta(minutes = mins)
    timeToMeet = startTime - minsDelta
    return timeToMeet

def getPrintableTime(time):
    return str(time.hour) + ":" + str(time.minute)

def getTimeStamp(start):
    startTime = stringTimeToDatetime(start)
    timestamp = (startTime - datetime.datetime(1970, 1, 1)).total_seconds()
    return timestamp

def waitUntilOneHourBeforeMeet(timeToMeet):
    minsDelta = datetime.timedelta(minutes = 60)
    timeToPost = timeToMeet - minsDelta
    delayDelta = timeToPost - datetime.datetime.utcnow()
    secondsToWait = delayDelta.total_seconds()
    if secondsToWait < 0:
        secondsToWait = 0
    print "waiting " + str(secondsToWait) + " seconds"
    time.sleep(secondsToWait)

def waitUntilNextAttempt(startTime):
    minsDelta = datetime.timedelta(minutes = 55)
    timeToPost = startTime - minsDelta
    delayDelta = timeToPost - datetime.datetime.utcnow()
    secondsToWait = delayDelta.total_seconds()
    if secondsToWait < 0:
        secondsToWait = 0
    print "waiting " + str(secondsToWait) + " seconds"
    time.sleep(secondsToWait)

def waitUntilAfterEvent(startTime):
    minsDelta = datetime.timedelta(minutes = 5)
    delayDelta = (startTime - datetime.datetime.utcnow()) + minsDelta
    secondsToWait = delayDelta.total_seconds()
    if secondsToWait < 0:
        secondsToWait = 0
    print "waiting " + str(secondsToWait) + " seconds"
    time.sleep(secondsToWait)

def main():
    defaultLocationString = "Starbucks -> "
    defaultTitleString = " meet for: "

    postTestMessage()

    while True:
        eventDetails = getNextEventDetails()

        timeToMeet = getTimeToMeet(eventDetails['start'],eventDetails['location'])
        if timeToMeet == "UNKNOWN":
            printableTimeToMeet = timeToMeet
        else:
            printableTimeToMeet = getPrintableTime(timeToMeet)
        titleString = printableTimeToMeet + defaultTitleString + eventDetails['summary']
        locationString = defaultLocationString + eventDetails['location']
        timestamp = getTimeStamp(eventDetails['start'])

        newPlan = Plan(timestamp,titleString, locationString)

        print " Next event: " + titleString
        waitUntilOneHourBeforeMeet(timeToMeet)
        postPlanToGroup(newPlan)
        print " posted about " + titleString
        waitUntilNextAttempt(stringTimeToDatetime(eventDetails['start']))
        postPlanToGroup(newPlan)
        print " posted about " + titleString

        waitUntilAfterEvent(stringTimeToDatetime(eventDetails['start']))



if __name__ == '__main__':
    main()
