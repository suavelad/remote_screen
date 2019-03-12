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

# Write a shell command and saves it in the output variable
imageNames = []
videoNames = []

fileImages = os.popen("gsutil ls -lh gs://media_2019/images | sort -k 2")
fileVideos = os.popen("gsutil ls -lh  gs://media_2019/videos | sort -k 2")

print("Image Names: ")
for imageName in fileImages.readlines():
    imageNames.append(imageName[23:len(imageName)-1])
    print((imageName[23:len(imageName)-1]))

print("****************")

# print("Video Names: ")
for videoName in fileVideos.readlines():
    videoNames.append(videoName[23:len(videoName)-1])
    print(videoName[23:len(videoName)-1])

print("Latest Upload: ")
# print(imageNames[-1][34:])
# print(videoNames[-1][34:])
LatestImage = imageNames[-1][34:]
LatestVideo = videoNames[-1][34:]
print(LatestImage)
print(LatestVideo)

MQTT_MSG = LatestImage + "," + LatestVideo


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