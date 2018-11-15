import RPi.GPIO as GPIO
import time

channel = 27
# GPIO Setup
GPIO.setmode(GPIO.BCM)
GPIO.setup(channel, GPIO.OUT)

def relay_on(pin):
    GPIO.output(pin, GPIO.HIGH)

def relay_off(pin):
    GPIO.output(pin, GPIO.LOW)

if __name__ == "__main__":
    try:
        while True:
            print(" am ON")
            relay_on(channel)
            time.sleep(2)
            print("Now Off")
            relay_off(channel)
            time.sleep(1)
            #GPIO.cleanup()
    except KeyboardInterrupt:
        print("Cleaning GPIO states...")
        GPIO.cleanup()
