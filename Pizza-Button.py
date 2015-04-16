import os
import RPi.GPIO as GPIO
import time
from get_pizza import*
GPIO.setmode(GPIO.BCM)
GPIO.setup(26,GPIO.IN, pull_up_down = GPIO.PUD_UP)

cpress=False
last_pressed=0 
wait_time=.5 # in seconds
while True:
	if(GPIO.input(26)==0):
		if (cpress==False):
			print("Button Pressed!")
			order_pizza("user_detail.txt")
			last_pressed=time.time()
		cpress=True
	elif(time.time()>last_pressed+wait_time):
		cpress=False
			

GPIO.cleanup()

