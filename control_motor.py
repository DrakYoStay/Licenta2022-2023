
import RPi.GPIO as GPIO
import time

# set up GPIO pins
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# define motor pins
motor1a = 17 # pin 18 controls motor 1a
motor1b = 27 # pin 23 controls motor 1b
motor2a = 23 # pin 24 controls motor 2a
motor2b = 22 # pin 25 controls motor 2b

# set up PWM on motor pins
GPIO.setup(motor1a, GPIO.OUT)
GPIO.setup(motor1b, GPIO.OUT)
GPIO.setup(motor2a, GPIO.OUT)
GPIO.setup(motor2b, GPIO.OUT)
motor1 = GPIO.PWM(motor1a, 100) # frequency of 100 Hz
motor2 = GPIO.PWM(motor2a, 100) # frequency of 100 Hz
motor1.start(0) # initial duty cycle of 0
motor2.start(0) # initial duty cycle of 0

# define robot movement functions
def forward(speed):
    motor1.ChangeDutyCycle(speed)
    motor2.ChangeDutyCycle(speed)
    GPIO.output(motor1b, GPIO.LOW)
    GPIO.output(motor2b, GPIO.LOW)

def backward(speed):
    motor1.ChangeDutyCycle(speed)
    motor2.ChangeDutyCycle(speed)
    GPIO.output(motor1b, GPIO.HIGH)
    GPIO.output(motor2b, GPIO.HIGH)

def left(speed):
    motor1.ChangeDutyCycle(speed)
    motor2.ChangeDutyCycle(speed)
    GPIO.output(motor1b, GPIO.HIGH)
    GPIO.output(motor2b, GPIO.LOW)

def right(speed):
    motor1.ChangeDutyCycle(speed)
    motor2.ChangeDutyCycle(speed)
    GPIO.output(motor1b, GPIO.LOW)
    GPIO.output(motor2b, GPIO.HIGH)

def stop():
    motor1.ChangeDutyCycle(0)
    motor2.ChangeDutyCycle(0)

