import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

led = 4

led = int(raw_input('Please provide the LED pin number: '))
GPIO.setup(led, GPIO.OUT)

flag = 0
while(True):
	input = raw_input("'y' for LED toggle, 'q' for exit\n")
	if(input == 'y'):
		if(flag == 0 ):
			GPIO.output(led, 1)
			flag =1
			print 'GPIO on'
		else:
			GPIO.output(led, 0)
			flag =0
			print 'GPIO off'
	elif(input == 'q'):
		break		
	

GPIO.cleanup()

