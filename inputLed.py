import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

red_led_pin = 17
green_led_pin = 18
blue_led_pin = 27

GPIO.setup(red_led_pin, GPIO.OUT)
GPIO.setup(green_led_pin, GPIO.OUT)
GPIO.setup(blue_led_pin, GPIO.OUT)

def turn_off():
    GPIO.output(red_led_pin, GPIO.LOW)
    GPIO.output(green_led_pin, GPIO.LOW)
    GPIO.output(blue_led_pin, GPIO.LOW)

try:
    while True:
        user_input = raw_input("Enter 'r' for Red LED, 'g' for Green LED, 'b' for Blue LED, or 'q' to quit: ")

        if user_input.lower() == 'r':
            turn_off()
            GPIO.output(red_led_pin, GPIO.HIGH)
        elif user_input.lower() == 'g':
            turn_off()
            GPIO.output(green_led_pin, GPIO.HIGH)
        elif user_input.lower() == 'b':
            turn_off()
            GPIO.output(blue_led_pin, GPIO.HIGH)
        elif user_input.lower() == 'q':
            turn_off()
            GPIO.cleanup()
            break
        else:
            print("Invalid input. Please enter 'r', 'g', 'b', or 'q'.")

except KeyboardInterrupt:
    turn_off()
    GPIO.cleanup()
