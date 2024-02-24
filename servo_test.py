from gpiozero import Servo
import time

servo = Servo(13)

# Function to set the servo angle
def set_servo_angle(angle):
    # Convert the angle to the pulse width
    pulse_width = int(angle * 2000 / 180) + 500
    # Set the servo pulse width

 while True:
        # Set the servo to 0 degrees
    servo.min()
    time.sleep(1)  # Wait 1 second
    # Set the servo to 90 degrees
    servo.max()
    time.sleep(1)  # Wait 1 second
    # Set the servo to 180 degrees
    servo.mid()
    time.sleep(1)  # Wait 1 second
        

