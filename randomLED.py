import RPi.GPIO as GPIO
import random
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(18,GPIO.OUT)
GPIO.setup(23,GPIO.OUT)

while True:
    GPIO.output(18,GPIO.HIGH)
    time.sleep(random.randint(1,5))
    GPIO.output(18,GPIO.LOW)
    time.sleep(random.randint(1,5))
    GPIO.output(23,GPIO.HIGH)
    time.sleep(random.randint(1,5))
    GPIO.output(23,GPIO.LOW)
    time.sleep(random.randint(1,5))
