# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import RPi.GPIO as GPIO
import time
from gpiozero import Buzzer

def ledAlert():
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.setup(18,GPIO.OUT)
    print ("LED on")
    GPIO.output(18,GPIO.HIGH)
    time.sleep(1)
    print ("LED off")
    GPIO.output(18,GPIO.LOW)
    
def soundAlert():
    buzzer = Buzzer(17)
    while True:
    buzzer.beep()
    
