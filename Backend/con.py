import os
import sys
import paho.mqtt.client as mqtt
from google.cloud import storage

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "/home/s/Documents/Projects/Remote_Screen/Media-606208d3d348.json"


# Instantiate a client
client = storage.Client()
bucket = client.get_bucket("media_2019")


    # print("Media File Download in progress")
    # print("File to download: " + fileName)
    # blob = bucket.blob(fileName)
    # blob.download_to_filename()
    # print("Media File Download Sucessful")

if __name__ == '__main__':

    #DOWNLOAD
    blob = bucket.blob("LGA.jpeg")
    blob.download_to_filename("Content/jf")
    print("Media File Download Sucessful")