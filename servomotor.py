import RPi.GPIO as GPIO
import time

# Set the GPIO pin that the servo motor is connected to
servo_pin = 18

# Set the frequency of the PWM signal (in Hz)
pwm_freq = 50


# Initialize the GPIO pins
GPIO.setmode(GPIO.BCM)
GPIO.setup(servo_pin, GPIO.OUT)

# Create a PWM object
pwm = GPIO.PWM(servo_pin, pwm_freq)

# Start the PWM signal
pwm.start(2)
try:
    while True:
        # Move the servo motor to 0 degrees
        pwm.ChangeDutyCycle(12)
        print("180 degree")
        # Wait for a second
        time.sleep(2)
        
        # Move the servo motor to 180 degrees
        pwm.ChangeDutyCycle(2)
        print("0 degree")
        # Wait for a second
        time.sleep(2)


# Clean up the GPIO pins when the program is interrupted
except KeyboardInterrupt:
    pwm.stop()
    GPIO.cleanup()
