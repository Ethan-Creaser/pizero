import pigpio
from gpiozero import LED
import time

SERVO_PIN = 12
led = LED(26)

pi = pigpio.pi()

print("Hardware revision ", pi.get_hardware_revision())
print("PIGPIO Version ", pi.get_pigpio_version())

# Function to set the servo angle
def set_servo_angle(angle):
    # Convert the angle to the pulse width
    pulse_width = int(angle)
    # Set the servo pulse width
    pi.set_servo_pulsewidth(SERVO_PIN, pulse_width)

try:
    angle = 500
    for i in range(5):
        angle += 100
        time.sleep(2)
        print(angle)
    set_servo_angle(0)

except KeyboardInterrupt:
    # Turn off the servo on Ctrl+C
    pi.set_servo_pulsewidth(SERVO_PIN, 0)
    # Disconnect from the pigpio daemon
    pi.stop()