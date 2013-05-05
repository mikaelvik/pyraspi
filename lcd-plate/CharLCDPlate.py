#!/usr/bin/python

from time import sleep
from Adafruit_CharLCDPlate import Adafruit_CharLCDPlate

class CharLCDPlate(Adafruit_CharLCDPlate):

  def __init__(self, bm=()):
    Adafruit_CharLCDPlate.__init__(self)
    self.backlight(self.OFF)
    if not bm or type(bm) != list:
      bm = []
    bm += [''] * (4 - len(bm))
    self.buttons = dict(
      left= (self.LEFT,  self.YELLOW, bm[0]),
      up=   (self.UP,    self.ON,     bm[1]),
      down= (self.DOWN,  self.TEAL,   bm[2]),
      right=(self.RIGHT, self.VIOLET, bm[3])
    )

  def message_bg(self, msg, bg=-1):
    self.clear()
    self.message(msg)
    if bg >= 0:
      self.backlight(bg)

  def slideLeft(self, steps=16, freq=.07):
    for i in range(steps):
      self.scrollDisplayLeft()
      sleep(freq)

  def messageSlideLeft(self, msg, bg=-1, steps=16):
    self.message_bg("\n".join([" " * steps + l for l in msg.split("\n")]), bg)
    self.slideLeft(steps)

  def toggle_backlight(self, repeat, col1, col2, freq=.15):
    for i in range(repeat):
      self.backlight(i % 2 and col1 or col2)
      sleep(freq)

  def start_wait(self, wait=True):
    while wait:
      if self.buttonPressed(self.SELECT):
        break

  def start_listen(self, wait=True, goodbye_msg=""):
    prev = -1
    while wait:
      if self.buttonPressed(self.SELECT):
        self.message_bg(goodbye_msg, bg=2)
        sleep(1.5)
        self.message_bg("", bg=0)
        break

      for button in self.buttons.values():
        if self.buttonPressed(button[0]):
          if button is not prev:
            self.message_bg(bg=button[1], msg=button[2])
            prev = button
          break


if __name__ == '__main__':
  lcd = CharLCDPlate([
    "Message left",
    " UUUUUP",
    "\n   DOWN",
    "\n       right msg"
  ])
  lcd.start_wait()
  lcd.messageSlideLeft("Demo starting\n    nooooo!!", bg=lcd.BLUE)
  lcd.toggle_backlight(10, 1, 2)
  lcd.start_listen(goodbye_msg="Fred ut.")


