import RPi.GPIO as GPIO
import time

port1 = 11
port2 = 10
pause = 0.2

def init():
	GPIO.setmode(GPIO.BOARD)
	GPIO.setup(port1, GPIO.OUT)
	GPIO.setup(port2, GPIO.OUT)

def pon(port):
	GPIO.output(port, GPIO.HIGH)
	
def poff(port):
	GPIO.output(port, GPIO.LOW)

def main():
	while(True):
		pon(port1)
		time.sleep(pause)
		pon(port2)
		time.sleep(pause)
		poff(port1)
		time.sleep(pause)
		poff(port2)
		time.sleep(pause)

try:
	init()
	main()
except KeyboardInterrupt:
	GPIO.cleanup()
