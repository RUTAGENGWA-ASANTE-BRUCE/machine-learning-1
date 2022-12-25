import RPi.GPIO as GPIO
import os
from time import sleep,time
trigPin = 7
echoPin = 11
def setup():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setwarnings(False)
    GPIO.setup (trigPin, GPIO.OUT)
    GPIO.setup (echoPin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
def endless_loop():
    setup()
    
    while(True):
            GPIO.output(trigPin, 0)
            sleep(0.000002)
            GPIO.output(trigPin, 1)
            sleep(0.00001)
            GPIO.output(trigPin, 0)
            #to prevent overwriting the previous one we give each taken image an time_stamp
            time_stamp=time()
            cmd1="cd .."
            cmd2 = "raspistill -t 30000 -tl 2000 -o Desktop/bruce"+str(time_stamp)+".jpg"
            cmd3="curl -X POST -F file=@bruce.jpg -F directory='Y1' -F sub-directory='RCA0351YHG'  http://192.168.0.82/dataHandler.php"
            os.system(cmd1)
            os.system(cmd2)
            os.system(cmd3)
            sleep(30)
            continue
endless_loop()