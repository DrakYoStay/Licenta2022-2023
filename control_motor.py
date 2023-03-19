import RPi.GPIO as gpio
import time

MOTORSTANGA_FATA = 17
MOTORSTANGA_SPATE = 27
MOTORDREAPTA_FATA = 23
MOTORDREAPTA_SPATE = 22
#initializare motoare
class Motoare():
    def __init__(self):
        gpio.setmode(gpio.BCM)
        gpio.setup(MOTORSTANGA_FATA, gpio.OUT)
        gpio.setup(MOTORSTANGA_SPATE, gpio.OUT)
        gpio.setup(MOTORDREAPTA_FATA, gpio.OUT)
        gpio.setup(MOTORDREAPTA_SPATE, gpio.OUT)


    def inainte(self):
        gpio.output(MOTORSTANGA_FATA, gpio.HIGH)
        gpio.output(MOTORSTANGA_SPATE, gpio.LOW)
        gpio.output(MOTORDREAPTA_FATA, gpio.HIGH)
        gpio.output(MOTORDREAPTA_SPATE, gpio.LOW)

    def inapoi(self):
        gpio.output(MOTORSTANGA_FATA, gpio.LOW)
        gpio.output(MOTORSTANGA_SPATE, gpio.HIGH)
        gpio.output(MOTORDREAPTA_FATA, gpio.LOW)
        gpio.output(MOTORDREAPTA_SPATE, gpio.HIGH)

    def stanga(self):
        gpio.output(MOTORSTANGA_FATA, gpio.LOW)
        gpio.output(MOTORSTANGA_SPATE, gpio.HIGH)
        gpio.output(MOTORDREAPTA_FATA, gpio.HIGH)
        gpio.output(MOTORDREAPTA_SPATE, gpio.LOW)

    def dreapta(self):
        gpio.output(MOTORSTANGA_FATA, gpio.HIGH)
        gpio.output(MOTORSTANGA_SPATE, gpio.LOW)
        gpio.output(MOTORDREAPTA_FATA, gpio.LOW)
        gpio.output(MOTORDREAPTA_SPATE, gpio.HIGH)

    def stop(self):
        gpio.output(MOTORSTANGA_FATA, gpio.LOW)
        gpio.output(MOTORSTANGA_SPATE, gpio.LOW)
        gpio.output(MOTORDREAPTA_FATA, gpio.LOW)
        gpio.output(MOTORDREAPTA_SPATE, gpio.LOW)
