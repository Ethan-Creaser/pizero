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
    pulse_width = int(angle)/180 * 1000 + 500

    # Set the servo pulse width
    pi.set_servo_pulsewidth(SERVO_PIN, pulse_width)

try:
    angle = 0
    #set_servo_angle(180)
    pi.set_servo_pulsewidth(SERVO_PIN, 600)
    time.sleep(2)
    pi.set_servo_pulsewidth(SERVO_PIN, 500)
    time.sleep(2)
    pi.set_servo_pulsewidth(SERVO_PIN,0)
    exit()
    for i in range(4):
        angle += 45
        time.sleep(2)
        set_servo_angle(angle)
        print(angle)

    set_servo_angle(0)
    time.sleep
    pi.set_servo_pulsewidth(SERVO_PIN, 0)

except KeyboardInterrupt:
    # Turn off the servo on Ctrl+C
    pi.set_servo_pulsewidth(SERVO_PIN, 0)
    # Disconnect from the pigpio daemon
    pi.stop()