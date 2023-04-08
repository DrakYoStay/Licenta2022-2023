import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

servo_pin = 18
GPIO.setup(servo_pin, GPIO.OUT)

servo = GPIO.PWM(servo_pin, 50) # set the PWM frequency to 50 Hz
servo.start(0) # start the PWM signal with 0 duty cycle (neutral position)

try:
    while True:
        for angle in range(0, 181, 10):
            duty_cycle = angle / 18.0 + 2.5 # convert angle to duty cycle (2.5 - 12.5)
            servo.ChangeDutyCycle(duty_cycle)
            time.sleep(0.05)

        for angle in range(180, -1, -10):
            duty_cycle = angle / 18.0 + 2.5 # convert angle to duty cycle (2.5 - 12.5)
            servo.ChangeDutyCycle(duty_cycle)
            time.sleep(0.05)

except KeyboardInterrupt:
    servo.stop()
    GPIO.cleanup()
