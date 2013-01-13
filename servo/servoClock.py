#!/usr/bin/python

from Adafruit_PWM_Servo_Driver import PWM
import time
from datetime import datetime

# ===========================================================================
# Example Code
# ===========================================================================

# Initialise the PWM device using the default address
# bmp = PWM(0x40, debug=True)
pwm = PWM(0x40, debug=True)

pwm.setPWMFreq(60)                        # Set frequency to 60 Hz

while (True):
	seconds = datetime.now().second 
	#scale
	moveTo = 200 + seconds*400/60
	pwm.setPWM(0, 0, moveTo)
	time.sleep(1)
