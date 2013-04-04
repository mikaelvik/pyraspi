#!/usr/bin/python

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
  for i in range(20):
    time.sleep(.1)
    all(i % 2)

blink()
all()

