import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)

pinForward = 17
pinBackward = 27

GPIO.setup(pinForward, GPIO.OUT)
GPIO.setup(pinBackward, GPIO.OUT)

p = GPIO.PWM(pinForward, 50)
q = GPIO.PWM(pinBackward, 50)

p.start(0)
p.ChangeDutyCycle(50)
sleep(5)
p.stop()

q.start(0)
q.ChangeDutyCycle(50)
sleep(5)
q.stop()

GPIO.cleanup()