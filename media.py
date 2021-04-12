import os
import random
import pprint

path = "/Media/"


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

song_list = []
allFiles = getListOfFiles(path)
for song in allFiles:
    if ".mp3" in song:
        song_list.append(song)
randomfile = random.choice(song_list)

print(randomfile)

input = "omxplayer "+randomfile
result = os.popen(gam_input).read()
print(result)
print("Done")
