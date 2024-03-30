# IR sensor interfacing

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(16,GPIO.IN)
GPIO.setup(3,GPIO.OUT)

while True:
    sen_val=GPIO.input(16)
    if sen_val==0:
        print('Object detected')
        GPIO.output(3,GPIO.HIGH)
        time.sleep(.5)
    else:
        print('Object not detected')
        GPIO.output(3,GPIO.LOW)
        time.sleep(.5)

GPIO.cleanup()
