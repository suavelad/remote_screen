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
    MediaFile = msg.payload.decode()
    if MediaFile in MediaFiles:
        print("Already exist")
        pass
    else: 
        MediaFiles.append(MediaFile)
        print("Media File Download in progress")
        print("File to download: " + MediaFile)
        blob = bucket.blob(MediaFile)
        blob.download_to_filename(MediaFile)
        blob.download_to_filename("Content/"+MediaFile)
        print("Media File Download Sucessful")
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
