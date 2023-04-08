import RPi.GPIO as GPIO
import time

# set up GPIO pins
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

motor_stanga_fata = 17
motor_stanga_spate = 27
motor_dreapta_fata = 22
motor_dreapta_spate = 23


GPIO.setup(motor_stanga_fata, GPIO.OUT)
GPIO.setup(motor_stanga_spate, GPIO.OUT)
GPIO.setup(motor_dreapta_fata, GPIO.OUT)
GPIO.setup(motor_dreapta_spate, GPIO.OUT)
motor_stanga_fwd = GPIO.PWM(motor_stanga_fata, 100)
motor_stanga_bwd = GPIO.PWM(motor_stanga_spate, 100)
motor_dreapta_fwd = GPIO.PWM(motor_dreapta_fata, 100)
motor_dreapta_bwd = GPIO.PWM(motor_dreapta_spate, 100)
motor_stanga_fwd.start(0)
motor_dreapta_fwd.start(0)
motor_stanga_bwd.start(0)
motor_dreapta_bwd.start(0)


def forward(speed):
    GPIO.output(motor_stanga_spate, GPIO.LOW)
    GPIO.output(motor_dreapta_spate, GPIO.LOW)
    motor_stanga_fwd.ChangeDutyCycle(speed)
    motor_dreapta_fwd.ChangeDutyCycle(speed)
    motor_stanga_bwd.ChangeDutyCycle(0)
    motor_dreapta_bwd.ChangeDutyCycle(0)

def backward(speed):
    GPIO.output(motor_stanga_fata, GPIO.LOW)
    GPIO.output(motor_dreapta_fata, GPIO.LOW)
    motor_stanga_fwd.ChangeDutyCycle(0)
    motor_dreapta_fwd.ChangeDutyCycle(0)
    motor_stanga_bwd.ChangeDutyCycle(speed)
    motor_dreapta_bwd.ChangeDutyCycle(speed)



def left(speed):
    GPIO.output(motor_stanga_spate, GPIO.LOW)
    GPIO.output(motor_dreapta_fata, GPIO.LOW)
    motor_stanga_fwd.ChangeDutyCycle(0)
    motor_dreapta_fwd.ChangeDutyCycle(speed)
    motor_stanga_bwd.ChangeDutyCycle(speed)
    motor_dreapta_bwd.ChangeDutyCycle(0)


def right(speed):
    GPIO.output(motor_stanga_fata, GPIO.LOW)
    GPIO.output(motor_dreapta_spate, GPIO.LOW)
    motor_stanga_fwd.ChangeDutyCycle(speed)
    motor_dreapta_fwd.ChangeDutyCycle(0)
    motor_stanga_bwd.ChangeDutyCycle(0)
    motor_dreapta_bwd.ChangeDutyCycle(speed)

def stop():
    motor_stanga_fwd.ChangeDutyCycle(0)
    motor_dreapta_fwd.ChangeDutyCycle(0)
    motor_stanga_bwd.ChangeDutyCycle(0)
    motor_dreapta_bwd.ChangeDutyCycle(0)

