#!/usr/bin/env python3

import os
import sys
import paho.mqtt.client as mqtt

# Define Variables
MQTT_HOST = "localhost"
MQTT_PORT = 1883
MQTT_KEEPALIVE_INTERVAL = 60
MQTT_TOPIC = "Media"
ImageFile = ''
VideoFile = ''

# This is the Subscriber


def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    mqttc.subscribe(MQTT_TOPIC)


def on_message(client, userdata, msg):
    FileNames = msg.payload.decode()
    mqttc.disconnect()
    ImageFile, VideoFile = FileNames.split(',')
    print(ImageFile)
    print(VideoFile)
    print("Download in progress")
    os.popen("gsutil cp gs://media_2019/images/"+ImageFile + " Content/")
    os.popen("gsutil cp gs://media_2019/videos/"+VideoFile + " Content/")

    
# Initiate MQTT Client
mqttc = mqtt.Client()

# Assign event callbacks
mqttc.on_message = on_message
mqttc.on_connect = on_connect
# mqttc.on_subscribe = on_subscribe


# Connect with MQTT Broker
mqttc.connect(MQTT_HOST, MQTT_PORT, MQTT_KEEPALIVE_INTERVAL)


# Continue monitoring the incoming messages for subscribed topic
mqttc.loop_forever()
