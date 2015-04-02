import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

led = 4

led = raw_input('Please provide the LED pin number:')
GPIO.setup(led, GPIO.OUT)

flag = 0
while(True):
	input = raw_input("'y' for LED toggle, 'q' for exit")
	if(input == 'y'):
		if(flag == 0 ):
			GPIO.output(led, 1)
		else:
			GPIO.output(led, 0)
	elif(input == 'q'):
		break		
	

GPIO.cleanup()

