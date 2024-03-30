# LED BLINKING 5 TIMES

import RPi.GPIO as GPIO
import time

# Set up GPIO using BOARD numbering
GPIO.setmode(GPIO.BOARD)

# Set GPIO pin 3 as output pin
GPIO.setup(3,GPIO.OUT)

# Blink LED 5 times
for i in range(5):
    GPIO.output(3,GPIO.HIGH)      # Turn on LED
    print('LED on')
    time.sleep(1)                  # Wait for 1 second
    GPIO.output(3,GPIO.LOW)        # Turn off LED
    print('LED off')
    time.sleep(1)                  # Wait for 1 second

# Clean up GPIO
GPIO.cleanup
