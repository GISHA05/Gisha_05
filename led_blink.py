# LED BLINKING

import RPi.GPIO as GPIO
import time


GPIO.setmode(GPIO.BOARD)
GPIO.setup(5,GPIO.OUT)

while 1:
    GPIO.output(5,GPIO.HIGH)
    print('LED on')
    time.sleep(1)
    GPIO.output(5,GPIO.LOW)
    print('LED off')
    time.sleep(1)

GPIO.cleanup()




















    
