import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(18,GPIO.OUT)

def on():
	print ("LED on")
	GPIO.output(18,GPIO.HIGH)

def off():
	print ("LED off")
	GPIO.output(18,GPIO.LOW)

while True:
	on()
	time.sleep(1)
	off()
	time.sleep(1)
