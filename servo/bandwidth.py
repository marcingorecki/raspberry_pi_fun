#!/usr/bin/python

from Adafruit_PWM_Servo_Driver import PWM
import time
from datetime import datetime


# Initialise the PWM device using the default address
# bmp = PWM(0x40, debug=True)
pwm = PWM(0x40, debug=True)

pwm.setPWMFreq(60)                        # Set frequency to 60 Hz
scaleMin = 200				  # Low angle
scaleMax = 400				  # Max movement
maxBandwidth = 2*1024*1024		  # 2MB/s

prev = -1

while (True):
	seconds = datetime.now().second 
	current = int(open('/sys/class/net/eth0/statistics/rx_bytes','r').read())
	if(prev == -1):
		#start with 0 speed
		prev = current
	bytes = current-prev
	#scale
	moveTo = scaleMin + bytes*scaleMax/maxBandwidth
	pwm.setPWM(0, 0, moveTo)
	#print "bytes %d" % bytes
	prev = current
	time.sleep(1)
