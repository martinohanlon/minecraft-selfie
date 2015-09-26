#Minecraft Selfie Cam
##Martin O'Hanlon (martin@ohanlonweb.com)
##http://www.stuffaboutcode.com

##Description
A program which takes a picture with either a PC webcam or the Raspberry Pi Camera and renders the image in Minecraft.

Image rendering code based on a project by Ferran Fabregas http://projectlog.ferranfabregas.info/rendering-pi-camera-pictures-into-minecraft-pi-world/

##Structure
* mcpi - minecraft pi python library
* mcselfiepc.py - PC python program
* mcselfiepi.py - Pi python program

##Pre-requisites
PC program requires 
* VideoCapture python library http://videocapture.sourceforge.net/

Pi program requires 
* the camera module
* picamera python library https://picamera.readthedocs.org/en/release-1.10/ 
* PIL, install with sudo apt-get install python-dev then sudo pip install Pillow


##Version history
* 0.1 - Initial stable version
