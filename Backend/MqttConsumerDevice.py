#!/usr/bin/env python3

'''
The receives the name of the last data upload of the cloud storage 
then it downloads that data using the name into the content folder
which will then be sorted and displayed on the advert screen using 
a media player. 

'''
import os
import sys
import paho.mqtt.client as mqtt
from google.cloud import storage

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "/home/s/Documents/Projects/Remote_Screen/Media-606208d3d348.json"


# Instantiate a client
client = storage.Client()
bucket = client.get_bucket("media_2019")

# Define Variables
MQTT_HOST = "localhost"
MQTT_PORT = 1883
MQTT_KEEPALIVE_INTERVAL = 60
MQTT_TOPIC = "Media"
MediaFiles = []

# This is the Subscriber


def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    mqttc.subscribe(MQTT_TOPIC)


def on_message(client, userdata, msg):
    mediaFile = msg.payload.decode()

    if ',' in mediaFile:
        imageFile, videoFile = mediaFile.split(",")
        print("Media file download in progress")
        MediaFiles.append(imageFile)
        MediaFiles.append(videoFile)
        print("Image file to download: " + imageFile)
        # print(type(imageFile))
        ImageBlob = bucket.blob(imageFile)
        ImageBlob.download_to_filename("Content/"+imageFile)
        print("Video file to download: " + videoFile)
        VideoBlob = bucket.blob(videoFile)
        VideoBlob.download_to_filename("Content/"+videoFile)

    else:
        MediaFiles.append(mediaFile)
        print("Media file to download: " + mediaFile)
        # print(type(mediaFile))
        MediaBlob = bucket.blob(mediaFile)
        MediaBlob.download_to_filename("Content/"+mediaFile)

    print("Media file download sucessful")
    print(" ")

# Initiate MQTT Client
mqttc = mqtt.Client()

# Assign event callbacks
mqttc.on_message = on_message
mqttc.on_connect = on_connect

# Connect with MQTT Broker
mqttc.connect(MQTT_HOST, MQTT_PORT, MQTT_KEEPALIVE_INTERVAL)

# Continue monitoring the incoming messages for subscribed topic
mqttc.loop_forever()
