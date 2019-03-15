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
VError = ''
IError = ''
imageNames = []
videoNames = []

while True :
    # Write a shell command and saves it in the output variable

    fileImages = os.popen("gsutil ls -lh gs://media_2019/images | sort -k 2")
    fileVideos = os.popen("gsutil ls -lh  gs://media_2019/videos | sort -k 2")

    # print("Image Names: ")
    for imageName in fileImages.readlines():
        imageNames.append(imageName[23:len(imageName)-1])
        # print((imageName[23:len(imageName)-1]))

    # print("****************")

    # print("Video Names: ")
    for videoName in fileVideos.readlines():
        videoNames.append(videoName[23:len(videoName)-1])
        # print(videoName[23:len(videoName)-1])

    print("Latest Upload: ")

    # LatestImage = imageNames[-1][34:]
    # LatestVideo = videoNames[-1][34:]
    # LatestImage = ''
    # LatestVideo = ''
    # print(LatestImage)
    # print(LatestVideo)

    if LatestImage == imageNames[-1][34:]:
        IError = 'True'
        print("Pass")
        pass
    else: 
        print("Image Publishing")
        LatestImage = imageNames[-1][34:]
        IError = 'False'
        print(LatestImage)

    if LatestVideo == videoNames[-1][34:]:
        VError = 'True'
        print("Pass")
        pass

    else:
        print("Video Publishing")
        LatestVideo = videoNames[-1][34:]
        VError = 'False'
        print(LatestVideo)

    if VError == 'True' and IError == 'False':
        MQTT_MSG = LatestImage
    
    elif IError == 'True' and VError == 'False':
        MQTT_MSG = LatestVideo
    
    elif (IError == 'True') and (IError == 'True'):
        MQTT_MSG = 'NaN'
    
    else:
        MQTT_MSG = LatestImage + "," + LatestVideo

    print(MQTT_MSG)


    # This is the Publisher

    # Define on_publish event function
    def on_publish(client, userdata, mid):
        print("Message Published...")

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