#!/usr/bin/python3

import RPi.GPIO as g
import time
import random

g.setmode(g.BOARD)
g.setwarnings(False)

pins = [11, 12, 13, 15, 16]

go = g.output
gs = g.setup

[gs(pin, 0) for pin in pins]

def off():
  [go(pin, 0) for pin in pins]
  print("all pins are off")

 
def svezza(): 
  for i in range(50):
    for j in pins:
      go(j, random.randint(0,1))
      time.sleep(.1)
    time.sleep(.1)

svezza()
off() 
