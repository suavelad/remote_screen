'''
The Mqtt Producer get the name of the last file uploaded
to the Google Cloud Storage.
'''

# Import needed packages
import os
import sys

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
print(imageNames[-1])
print(videoNames[-1])
