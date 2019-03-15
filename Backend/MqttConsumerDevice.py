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

os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="/home/s/Documents/Projects/Remote_Screen/Media-606208d3d348.json"




# Instantiate a client
client = storage.Client()
bucket = client.get_bucket("media_2019")


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
    
    if "," in FileNames:
        ImageFile, VideoFile = FileNames.split(',')
        print("Contents: ")
        print(ImageFile)
        print(VideoFile)
        print("Download in progress")
        # os.popen("gsutil cp gs://media_2019/images/"+ImageFile + " Content/")
        # os.popen("gsutil cp gs://media_2019/videos/"+VideoFile + " Content/")
        ImageBlob = bucket.blob('images/'+ImageFile)
        VideoBlob = bucket.blob('videos/'+VideoFile)
        ImageBlob.download_to_filename('Content/'+ImageFile)
        VideoBlob.download_to_filename('Content/'+VideoFile)
        print(" Download Sucessful")
        # mqttc.disconnect()

    elif '.mp4' in FileNames:
        VideoFile = FileNames
        print(VideoFile)
        print("Video Download in progress")
        VideoBlob = bucket.blob('videos/'+VideoFile)
        VideoBlob.download_to_filename('Content/'+VideoFile)
        print("Video Download Sucessful")
        # mqttc.disconnect()
    
    
    elif ('.jpg') in FileNames:
        ImageFile = FileNames
        print(ImageFile)
        print("Image Download in progress")
        ImageBlob = bucket.blob('images/'+ImageFile)
        ImageBlob.download_to_filename('Content/'+ImageFile)
        print("Image Download Sucessful")

        # mqttc.disconnect()
    # elif FileNames == 'NaN':
    #     print('pass')
    #     pass
        
    else:
        # print('pass')
        pass

# Initiate MQTT Client
mqttc = mqtt.Client()

# Assign event callbacks
mqttc.on_message = on_message
mqttc.on_connect = on_connect

# Connect with MQTT Broker
mqttc.connect(MQTT_HOST, MQTT_PORT, MQTT_KEEPALIVE_INTERVAL)

# Continue monitoring the incoming messages for subscribed topic
mqttc.loop_forever()
