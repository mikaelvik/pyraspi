import RPi.GPIO as g

g.setmode(g.BOARD)
g.setwarnings(False)

gs = g.setup
go = g.output
gi = g.input

pins = [11, 12, 13]
[gs(pin, 0) for pin in pins]

def on():
  [go(pin, 1) for pin in pins]

def off():
  [go(pin, 0) for pin in pins]

def switch(channel):
  if gi(channel):
    on()
  else:
    off()

g.add_event_detect(7, g.BOTH, callback=switch, bouncetime=50)

