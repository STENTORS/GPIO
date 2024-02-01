import RPi.GPIO as GPIO
import time

GPIO.setmode(BCM)
GPIO.setup(18,GPIO.OUT)
GPIO.setup(23,GPIO.OUT)

while True:
    try:
        GPIO.output(18,GPIO.HIGH)
        time.sleep(1)
        GPIO.output(18,GPIO.LOW)
        GPIO.output(23,GPIO.HIGH)
        time.sleep(1)
        GPIO.output(23,GPIO.LOW)
        except ValueError:
            break
            
