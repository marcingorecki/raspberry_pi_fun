#!/usr/bin/python

from Adafruit_PWM_Servo_Driver import PWM
import time
import sys

# ===========================================================================
# Wave the Flag!
# http://youtu.be/oCivzMOjH3s
# ===========================================================================

# Initialise the PWM device using the default address
# bmp = PWM(0x40, debug=True)
pwm = PWM(0x40, debug=True)

servoMin = 200  # Min pulse length out of 4096
servoMax = 600  # Max pulse length out of 4096

pwm.setPWMFreq(60)                        # Set frequency to 60 Hz

#scale
def move(moveTo):
	moveTo = servoMin+moveTo*servoMax/100
	pwm.setPWM(0, 0, moveTo)

while (True):
	move(20)
	time.sleep(0.4)
	move(60)
	time.sleep(0.4)

