#used USBMOUNT to auto mount USBs, modified to add exfat file type
#set audio output to 3.5 mm and made sure volume was turned up
#instaled omxplayer


#what did we use to set the volume?

import time
import os
import random
import pprint

path = "/media/usb0"

played_songs = []

def getListOfFiles(dirName):
    # create a list of file and sub directories
    # names in the given directory
    listOfFile = os.listdir(dirName)
    allFiles = list()
    # Iterate over all the entries
    for entry in listOfFile:
        # Create full path
        fullPath = os.path.join(dirName, entry)
        # If entry is a directory then get the list of files in this directory
        if os.path.isdir(fullPath):
            allFiles = allFiles + getListOfFiles(fullPath)
        else:
            allFiles.append(fullPath)

    return allFiles

def play():
    song_list = []
    allFiles = getListOfFiles(path)
    print(played_songs)
    print("***")

    for song in allFiles:
        if ".mp3" in song:
            #print("Found Song:,",song)
            if song not in played_songs:
                song_list.append(song)
    if song_list:
        randomfile = random.choice(song_list)
    else:
        print("Cannot get songs")
        time.sleep(5)
        print("Quitting!")
        exit()

    print("Playing:",randomfile)

    input = 'omxplayer -o local "'+randomfile+'"'
    result = os.popen(input).read()
    print(result)
    print("Done Playing")
    return randomfile

while True:
    played_songs.append (play())
