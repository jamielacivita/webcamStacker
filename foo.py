import requests
import datetime

def printResponseHeaders(rh):
    for n in rh:
        print(n, rh[n])

def writeFile(rawcontent):
    print("writing the image")
    path = r"./"
    filemane = r"downloadedPic" + makeTimestamp() + r".jpeg"
    URL = path + filemane
    with open(URL, "wb") as f:
        f.write(rawcontent)
    f.close()
    print("image written")

def makeTimestamp():
    now = datetime.datetime.now()
    #timestamp = str(now.year) + str(now.month) + str(now.day) + str(now.hour) + str(now.min) + str(now.second)
    #timestamp = str(now.year) + str(now.month) + str(now.day) + "_" + str(now.hour)

    timestamp = now.strftime("%y%m%d_%H%M%S")

    return timestamp

print("Hello World")
#https://photos.bogusbasin.org/flats.php
#https://photos.bogusbasin.org/coaster.php
#https://cam.discoversawtooth.org/camera/camera0.jpg

URL = r"https://photos.bogusbasin.org/flats.php"
response = requests.get(URL, verify=False)
print(response.status_code)
printResponseHeaders(response.headers)
writeFile(response.content)

#print(makeTimestamp())










