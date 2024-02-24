import pigpio
import time

servo = 13

pwm = pigpio.pi()
pwm.set_mode(servo, pigpio.OUTPUT)
print("Hardware revision ",pwm.get_hardware_revision())
print("PIGPIO Version ",pwm.get_pigpio_version())

pwm.set_PWM_frequency(servo, 50)
pwm.set_PWM_range(servo, 20000)  # 1,000,000 / 50 = 20,000us for 100% duty cycle

pwm.hardware_PWM(servo, 50, 2000)
time.sleep(10)

pwm.set_servo_pulsewidth(servo, 0)