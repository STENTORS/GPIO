import RPi.GPIO as GPIO
import time

GPIO.setmode(BCM)
GPIO.setup(18,GPIO.OUT)
GPIO.setup(23,GPIO.OUT)

while True:
    try:
        colour = int(input("Colour (1)red, (2)while, (3)both"))
        if colour == 1:
            GPIO.output(18,GPIO.HIGH)
            time.sleep(1)
            GPIO.output(18,GPIO.LOW)
        elif colour == 2:
            GPIO.output(23,GPIO.HIGH)
            time.sleep(1)
            GPIO.output(23,GPIO.LOW)
        elif colour == 3:
            GPIO.output(23,GPIO.HIGH)
            GPIO.output(18,GPIO.HIGH)
            time.sleep(1)
            GPIO.output(23,GPIO.LOW)
            GPIO.output(18,GPIO.LOW)
        except ValueError:
            break
            

