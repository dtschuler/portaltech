import RPi.GPIO as GPIO
import time
import picamera
import datetime
import os
import sys

sys.path.append('object_detectionAPI')
from objdetect_utils import test_image_demo


def gpio_button_pictures():
    #Set up GPIO button to detect door open or closed
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(18, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
    GPIO.add_event_detect(18, GPIO.BOTH)
    #Init pi camera
    cam = picamera.PiCamera()
    cam.resolution = (360,480)

    print("=== Start ===")
    count = 0

    #loop to capture images as door opens and closes
    while True:
    #When GPIO pin changes states if = True
        if GPIO.event_detected(18):
            #Incr state
            count += 1
            #Mod to keep state between 0 (Close) and 1 (Open)
            count %= 2
            
            #When door opens take photo 
            if count == 1:
                print('Door Open')
                cam.capture('/tmp/open.jpg')
            #When door closes take phot and send to S3 bucket
            if count == 0:
                print('Door Closed')
                cam.capture('/tmp/close.jpg')
                test_image_demo('/tmp/')

if __name__ == '__main__':
        gpio_button_pictures()


    
