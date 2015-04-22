#Filename: gpioArg.py
#Author: Shien Hong 
#Description: GPIO pin toggle using the arguments

#import libraries
import RPi.GPIO as GPIO
import time
import sys

#Configure the GPIO pin
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

#Assign LED pin

if len(sys.argv) != 2:
    raise ValueError("Arm not found")

led = str(sys.argv[1])
switch = str(sys.argv[2])
GPIO.setup(led, GPIO.OUT)

#toggle or reset the GPIO pins
if switch == 'on':
	GPIO.output(led, 1)
elif switch == 'off':
	GPIO.output(led, 0)
elif switch == 'reset':
	GPIO.cleanup()
else:
	print 'wrong second argument'
		
	
	


