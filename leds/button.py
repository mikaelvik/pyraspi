#!/usr/bin/python3

import RPi.GPIO as g

g.setmode(g.BOARD)
g.setwarnings(False)
gs, go, gi = g.setup, g.output, g.input

pins = [11, 12, 13]
[gs(pin, 0) for pin in pins]
gs(7, 1, pull_up_down=g.PUD_DOWN)

def switch(pin=0, value=0):
  if pin:
    go(pin, value)
  else:
    [go(pin, value) for pin in pins]

def on(pin=0):
  switch(pin, value=1)

def off(pin=0):
  switch(pin, value=0)


active = 0
def button_pressed(channel):
  if gi(channel):
    global active
    off()
    on(pins[active % len(pins)])
    active +=1


g.add_event_detect(7, g.BOTH, callback=button_pressed, bouncetime=50)

