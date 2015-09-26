# Martin O'Hanlon
# www.stuffaboutcode.com
# Minecraft Selfie Camera
# Minecraft Picture Rendering Script By Ferran Fabregas (ferri.fc@gmail.com)

import picamera
from PIL import Image
import math
from mcpi.minecraft import Minecraft
from time import sleep, time

def takePicture(filename):
    with picamera.PiCamera() as camera:
        camera.start_preview(alpha=192)
        sleep(1)
        camera.capture(filename)
        camera.stop_preview()

def colormap(pixel):
    white=(221,221,221)
    orange=(219,125,62)
    magenta=(179,80,188)
    lightblue=(107,138,201)
    yellow=(177,166,39)
    lime=(65,174,56)
    pink=(208,132,153)
    gray=(64,64,64)
    lightgray=(154,161,161)
    cyan=(46,110,137)
    purple=(126,61,181)
    blue=(46,56,141)
    brown=(79,50,31)
    green=(53,70,27)
    red=(150,52,48)
    black=(25,22,22)

    colors=(white,orange,magenta,lightblue,yellow,lime,pink,gray,lightgray,cyan,purple,blue,brown,green,red,black)

    thecolor=0
    finalresult=256*256*256
    for idx,color in enumerate(colors):
        result=math.fabs(color[0]-pixel[0])+math.fabs(color[1]-pixel[1])+math.fabs(color[2]-pixel[2])
        if result<finalresult:
            finalresult=result
            thecolor=idx
    return thecolor


def buildMCImage(mc, filename, pos):

    MAXY = 60
    im = Image.open(filename)

    #resize image file
    if im.size[1] > MAXY:
        ratio = MAXY / float(im.size[1])
        sizeY = MAXY
        sizeX = int(im.size[0] * ratio)
        size = sizeX, sizeY
        im.thumbnail(size, Image.ANTIALIAS)
    
    pixels=im.load()

    for x in range (-(im.size[0]/2),(im.size[0]/2)):
        for y in range (0,(im.size[1])):
            mc.setBlock(pos.x + x, pos.y + sizeY - y, pos.z - 1, 35,
                        colormap(pixels[x+(im.size[0]/2) , y]))

            #print "{}.{}.{}".format(x, y, 5)
            sleep(0.005)


mc=Minecraft.create()
mc.postToChat("Welcome to Minecraft Camera")
mc.postToChat("Hit a block (right click with sword)")

while True:
    #has a block been hit?
    for hit in mc.events.pollBlockHits():
        filename = "/home/pi/" + str(int(time())) + ".png"
        mc.postToChat("Taking picture in 1 second")
        sleep(1)
        takePicture(filename)
        mc.postToChat("Building image")
        buildMCImage(mc, filename, hit.pos)
        mc.postToChat("Image built")

        #clear any block hit events
        mc.events.clearAll()

        break
    sleep(0.1)
