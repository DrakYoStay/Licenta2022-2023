import RPi.GPIO as GPIO
import time

# set up GPIO pins
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

motor1a = 17
motor1b = 27
motor2a = 22
motor2b = 23


GPIO.setup(motor1a, GPIO.OUT)
GPIO.setup(motor1b, GPIO.OUT)
GPIO.setup(motor2a, GPIO.OUT)
GPIO.setup(motor2b, GPIO.OUT)
motor1 = GPIO.PWM(motor1a, 20)
motor2 = GPIO.PWM(motor2a, 20)
motor1.start(0)
motor2.start(0)


def forward(speed):
    motor1.ChangeDutyCycle(speed)
    motor2.ChangeDutyCycle(speed)
    GPIO.output(motor1b, GPIO.LOW)
    GPIO.output(motor2b, GPIO.LOW)

def backward(speed):
    motor1.ChangeDutyCycle(speed)
    motor2.ChangeDutyCycle(speed)
    GPIO.output(motor1a, GPIO.LOW)
    GPIO.output(motor2a, GPIO.LOW)

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

