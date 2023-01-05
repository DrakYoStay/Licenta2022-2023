import RPi.GPIO as gpio

MOTORSTANGA_FATA = 17
MOTORSTANGA_SPATE = 22
MOTORDREAPTA_FATA = 23
MOTORDREAPTA_SPATE = 24
#initializare motoare
class Motoare():
    def __init__(self):
        gpio.setmode(gpio.BCM)
        gpio.setup(MOTORSTANGA_FATA, gpio.OUT)
        gpio.setup(MOTORSTANGA_SPATE, gpio.OUT)
        gpio.setup(MOTORDREAPTA_FATA, gpio.OUT)
        gpio.setup(MOTORDREAPTA_SPATE, gpio.OUT)

        self.pwm1a = gpio.PWM(MOTORSTANGA_FATA, 2000)
        self.pwm1b = gpio.PWM(MOTORSTANGA_SPATE, 2000)
        self.pwm2a = gpio.PWM(MOTORDREAPTA_FATA, 2000)
        self.pwm2b = gpio.PWM(MOTORDREAPTA_SPATE, 2000)

    def inainte(self):
        self.pwm1a.start(100)
        self.pwm1b.start(100)
        self.pwm2a.start(100)
        self.pwm2b.start(100)

        gpio.output(MOTORSTANGA_FATA, gpio.HIGH)
        gpio.output(MOTORSTANGA_SPATE, gpio.LOW)
        gpio.output(MOTORDREAPTA_FATA, gpio.HIGH)
        gpio.output(MOTORDREAPTA_SPATE, gpio.LOW)

    def inapoi(self):
        self.pwm1a.start(100)
        self.pwm1b.start(100)
        self.pwm2a.start(100)
        self.pwm2b.start(100)

        gpio.output(MOTORSTANGA_FATA, gpio.LOW)
        gpio.output(MOTORSTANGA_SPATE, gpio.HIGH)
        gpio.output(MOTORDREAPTA_FATA, gpio.LOW)
        gpio.output(MOTORDREAPTA_SPATE, gpio.HIGH)

    def stanga(self, dist):
        self.pwm1a.start(dist)
        self.pwm1b.start(dist)
        self.pwm2a.start(dist)
        self.pwm2b.start(dist)

        gpio.output(MOTORSTANGA_FATA, gpio.LOW)
        gpio.output(MOTORSTANGA_SPATE, gpio.HIGH)
        gpio.output(MOTORDREAPTA_FATA, gpio.HIGH)
        gpio.output(MOTORDREAPTA_SPATE, gpio.LOW)

    def dreapta(self, dist):
        self.pwm1a.start(dist)
        self.pwm1b.start(dist)
        self.pwm2a.start(dist)
        self.pwm2b.start(dist)

        gpio.output(MOTORSTANGA_FATA, gpio.HIGH)
        gpio.output(MOTORSTANGA_SPATE, gpio.LOW)
        gpio.output(MOTORDREAPTA_FATA, gpio.LOW)
        gpio.output(MOTORDREAPTA_SPATE, gpio.HIGH)

    def stop(self):
        gpio.output(MOTORSTANGA_FATA, gpio.LOW)
        gpio.output(MOTORSTANGA_SPATE, gpio.LOW)
        gpio.output(MOTORDREAPTA_FATA, gpio.LOW)
        gpio.output(MOTORDREAPTA_SPATE, gpio.LOW)