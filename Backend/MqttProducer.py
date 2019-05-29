#!/usr/bin/env python3
'''
The Mqtt Producer get the name of the last file uploaded
to the Google Cloud Storage.
'''

# Import needed packages
import os
import sys
import paho.mqtt.client as mqtt

# Define Variables
MQTT_HOST = "localhost"
MQTT_PORT = 1883
MQTT_KEEPALIVE_INTERVAL = 60
MQTT_TOPIC = "Media"

LatestImage = ''
LatestVideo = ''
LatestFile = ''
VError = ''
IError = ''
Error = ''
imageNames = []
fileNames = []
videoNames = []

print("Latest File Uploaded: ")
while True :
    # Write a shell command and saves it in the output variable

    # fileImages = os.popen("gsutil ls -lh gs://media_2019/images | sort -k 2")
    # fileVideos = os.popen("gsutil ls -lh  gs://media_2019/videos | sort -k 2")
    files = os.popen("gsutil ls -lh  gs://media_2019 | sort -k 2")

    for fileName in files.readlines():
        fileNames.append(fileName[50:-1])
        # print((fileName[50:-1]))

    if LatestFile == fileNames[-1]:
        # Error = 'True'
        # print("Pass")
        pass

    else: 
        print(" Publishing Media Content...")
        LatestFile = fileNames[-1]
        # Error = 'False'
        MQTT_MSG = LatestFile
        print(LatestFile)
    # if LatestImage == imageNames[-1][34:]:
    #     IError = 'True'
    #     # print("Pass")
    #     pass

    # else: 
    #     print("Image Publishing...")
    #     LatestImage = imageNames[-1][34:]
    #     IError = 'False'
    #     print(LatestImage)

    # if LatestVideo == videoNames[-1][34:]:
    #     VError = 'True'
    #     # print("Pass")
    #     pass

    # else:
    #     print("Video Publishing...")
    #     LatestVideo = videoNames[-1][34:]
    #     VError = 'False'
    #     print(LatestVideo)

   
    # if VError == 'True' and IError == 'False':
    #     MQTT_MSG = LatestImage
    
    # elif IError == 'True' and VError == 'False':
    #     MQTT_MSG = LatestVideo
    
    # elif (IError == 'True') and (IError == 'True'):
    #     MQTT_MSG = 'NaN'
    
    # else:
    #     MQTT_MSG = LatestImage + "," + LatestVideo
    # print("*****************")
    # print("Files for publishing:  ")


    # This is the Publisher

    # Define on_publish event function
    def on_publish(client, userdata, mid):
        print("Message Published...")
        print (" ")

    # Initiate MQTT Client
    client = mqtt.Client()

    # Register publish callback function
    client.on_publish = on_publish

    # Connect with MQTT Broker
    client.connect(MQTT_HOST, MQTT_PORT, MQTT_KEEPALIVE_INTERVAL) 

    # Publish message to MQTT Broker 
    client.publish(MQTT_TOPIC, MQTT_MSG)

    # Disconnect from MQTT_Broker
    client.disconnect()