import pigpio
import time

SERVO_PIN = 13

pi = pigpio.pi()
pi.set_mode(servo, pigpio.OUTPUT)
print("Hardware revision ", pi.get_hardware_revision())
print("PIGPIO Version ", pi.get_pigpio_version())

# Function to set the servo angle
def set_servo_angle(angle):
    # Convert the angle to the pulse width
    pulse_width = int(angle * 2000 / 180) + 500
    # Set the servo pulse width
    pi.set_servo_pulsewidth(SERVO_PIN, pulse_width)

try:
    while True:
        # Set the servo to 0 degrees
        set_servo_angle(0)
        time.sleep(1)  # Wait 1 second
        # Set the servo to 90 degrees
        set_servo_angle(90)
        time.sleep(1)  # Wait 1 second
        # Set the servo to 180 degrees
        set_servo_angle(180)
        time.sleep(1)  # Wait 1 second
except KeyboardInterrupt:
    # Turn off the servo on Ctrl+C
    pi.set_servo_pulsewidth(SERVO_PIN, 0)
    # Disconnect from the pigpio daemon
    pi.stop()