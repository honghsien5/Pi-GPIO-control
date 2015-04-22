#Filename: pi_gpio.py 
#Author: Shien Hong 
#Description: GPIO pin toggling

#import libraries
import RPi.GPIO as GPIO
import time
import sys

#Configure the GPIO pin
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

#Assign LED pin
led = int(raw_input('Please provide the LED pin number: '))
GPIO.setup(led, GPIO.OUT)

flag = 0
GPIO.output(led,0)
#start the loop
while(True):
	#input for the input toggle
	input = raw_input("'y' for LED toggle, 'q' for exit\n")
	if(input == 'y'): #if input is 'y' toggle pin's output
		if(flag == 0 ):
			#turn light on and change the flag
			GPIO.output(led, 1)
			flag =1
			print 'GPIO on'
		else:
			#turn light off and change the flag
			GPIO.output(led, 0)
			flag =0
			print 'GPIO off'
	elif(input == 'q'):  #exit the program
		break		
	
#clean up the GPIO setting to prevent future conflict
GPIO.output(led,0)
GPIO.cleanup()

