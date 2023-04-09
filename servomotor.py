import RPi.GPIO as GPIO
import time

# Set the GPIO pin that the servo motor is connected to
servo_pin = 18

# Set the frequency of the PWM signal (in Hz)
pwm_freq = 50

# Set the duty cycle for the minimum and maximum positions of the servo motor (in %)
servo_min_duty = 2.5
servo_max_duty = 12.5

# Initialize the GPIO pins
GPIO.setmode(GPIO.BCM)
GPIO.setup(servo_pin, GPIO.OUT)

# Create a PWM object
pwm = GPIO.PWM(servo_pin, pwm_freq)

# Start the PWM signal
pwm.start(0)

# Function to move the servo motor to a specific angle
def set_servo_angle(angle):
    # Convert the angle to a duty cycle
    duty_cycle = servo_min_duty + (angle / 180.0) * (servo_max_duty - servo_min_duty)
    
    # Move the servo motor to the desired angle
    pwm.ChangeDutyCycle(duty_cycle)
    
    # Wait for the servo motor to move
    time.sleep(0.5)

# Move the servo motor from 0 degrees to 180 degrees and back to 0 degrees
try:
    while True:
        # Move the servo motor to 0 degrees
        set_servo_angle(0)
        
        # Wait for a second
        time.sleep(1)
        
        # Move the servo motor to 180 degrees
        set_servo_angle(180)
        
        # Wait for a second
        time.sleep(1)
        
        # Move the servo motor to 0 degrees
        set_servo_angle(0)
        
        # Wait for a second
        time.sleep(1)

# Clean up the GPIO pins when the program is interrupted
except KeyboardInterrupt:
    pwm.stop()
    GPIO.cleanup()
