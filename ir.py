# IR sensor interfacing

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(16,GPIO.IN)
#GPIO.setup(3,GPIO.IN)

while True:
    sen_val=GPIO.input(16)
    if sen_val==False:
        print('Object detected')
    time.sleep(.2)

GPIO.cleanup()



    
