import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

pins = [11, 12, 13, 15, 16]

go = GPIO.output
gs = GPIO.setup

[gs(pin, 0) for pin in pins]

def all(on=0):
  [go(pin, on) for pin in pins]

def blink():
  for i in range(30):
    for pin in pins:
      time.sleep(.02)
      go(pin, i % 2)
    time.sleep(.03)

blink()
all()

