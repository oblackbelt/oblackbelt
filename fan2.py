#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import time
import signal
import sys
import RPi.GPIO as GPIO

programled = 21
fanled = 27 # indicator led
pin = 14 # The pin ID, edit here to change it
maxTMP = 60 # The maximum temperature in Celsius after which we trigger the fan

try:
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(pin, GPIO.OUT)
    GPIO.setup(fanled, GPIO.OUT)
    GPIO.setup(programled, GPIO.OUT)
#    GPIO.setwarnings(False)

    while True:
        GPIO.output(programled, True)
        time.sleep(60)
        res = os.popen("vcgencmd measure_temp").readline()
        CPU_temp = float((res.replace("temp=","").replace("'C\n","")))
        print(CPU_temp) #Uncomment here for testing

        if CPU_temp < maxTMP:
            GPIO.output(pin, False)
            GPIO.output(fanled, False)
        else:
            GPIO.output(pin, True)
            GPIO.output(fanled, True)

except KeyboardInterrupt: # trap a CTRL+C keyboard interrupt 
    GPIO.cleanup() # resets all GPIO ports used by this program

#Game over
