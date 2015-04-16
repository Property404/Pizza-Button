#!/usr/bin/env python
# Import modules
import os
import RPi.GPIO as GPIO
import time
import urllib2
import get_pizza

# Global constants
USER_DETAIL_FILE="user_detail.xml"
SERIAL_NO_FILE="serial.txt" 

# Check network connection
def checkConnection():
	try:
		urllib2.urlopen('http://74.125.228.100') # Google
		return True
	except urllib2.URLError as err:
		print(err.args)
	return False

# Check activation for product
def checkActivation():
	try:
		open(USER_DETAIL_FILE,"r")
		return True
	except:
		return False


# Set up IO
GPIO.setmode(GPIO.BCM)
GPIO.setup(26,GPIO.IN, pull_up_down = GPIO.PUD_UP)

# Set up variables
cpress=False
last_pressed=0 
wait_time=.5 # in seconds

# Starting up
print "Starting..."
print "Connected: "+str(checkConnection())
print "Activated: "+str(checkActivation())

# Run loop to check for button press
while True:
	if(GPIO.input(26)==0):
		if (cpress==False):
			# Button confirmed pressed
			print("\nButton Pressed!")
			last_pressed=time.time()
			if checkConnection():
				# Check activation status
				if checkActivation():
					# Start ordering pizza
					get_pizza.order_pizza(USER_DETAIL_FILE)
				else:
					print("Not activated")
			else:
				print "Could not connect to network"
		cpress=True
	elif(time.time()>last_pressed+wait_time):
		cpress=False
			
# Finsih
GPIO.cleanup()

