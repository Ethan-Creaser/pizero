from gpiozero import LED
from time import sleep

led = LED(26) # Choose the correct pin number

while True:
    led.on()
    sleep(1)
    led.off()
    sleep(1)
