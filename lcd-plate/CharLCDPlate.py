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
      left= dict(button=self.LEFT,  bg=self.YELLOW, msg=bm[0]),
      up=   dict(button=self.UP,    bg=self.ON,     msg=bm[1]),
      down= dict(button=self.DOWN,  bg=self.TEAL,   msg=bm[2]),
      right=dict(button=self.RIGHT, bg=self.VIOLET, msg=bm[3])
    )

  def set_button(self, **buttons):
    """Set new values for one or more buttons.
    Example: set_button(left=dict(bg=3, msg="New message"))
    """
    for key, value in buttons.items():
      self.buttons[key].update(value)

  def message_bg(self, msg, bg=-1, **ignored):
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
        if self.buttonPressed(button['button']):
          if button is not prev:
            self.message_bg(**button)
            prev = button
          break

  def off(self):
    self.clear()
    self.backlight(self.OFF)


if __name__ == '__main__':
  lcd = CharLCDPlate([
    "Message left",
    " UUUUUP",
    "\n   DOWN",
    "\n       right msg"
  ])
  lcd.set_button(up=dict(msg="different up\nmessage"), right=dict(bg=lcd.RED))
  lcd.start_wait()
  lcd.messageSlideLeft("Demo starting\n    nooooow!!", bg=lcd.BLUE)
  lcd.toggle_backlight(10, 1, 2)
  lcd.start_listen(goodbye_msg="Fred ut.")


