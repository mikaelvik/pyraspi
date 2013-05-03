from time import sleep
from Adafruit_CharLCDPlate import Adafruit_CharLCDPlate

lcd = Adafruit_CharLCDPlate()
template = "                %s\n                %s"
welcome = template % ("FIRST LINE", "     OH YEE!!")
goodbye = "thank you\n   GOODBYE!"
no_start_wait, no_end_wait = 0, 0

lm = lcd.message
lb = lcd.backlight
cls = lcd.clear
lsl = lcd.scrollDisplayLeft
lsr = lcd.scrollDisplayRight

lb(0)

def slide_in():
  for i in range(16):
    lsl()
    sleep(.07)

def toggle_backlight(r, a=2, b=1):
  for i in range(r):
    lb(i % 2 and a or b)
    sleep(.15)

while True:
  if no_start_wait or lcd.buttonPressed(lcd.SELECT):
    break

lb(5)
lm(welcome)
slide_in()
toggle_backlight(6)

col = (lcd.RED , lcd.YELLOW, lcd.GREEN, lcd.TEAL,
       lcd.BLUE, lcd.VIOLET, lcd.ON   , lcd.OFF)

# Poll buttons, display message & set backlight accordingly
buttons = ((lcd.LEFT  , lcd.YELLOW, "left msg"),
           (lcd.UP    , lcd.ON,     "up msg"),
           (lcd.DOWN  , lcd.TEAL,   "down msg"),
           (lcd.RIGHT , lcd.VIOLET, "right msg"))
prev = -1
while True:
  if no_end_wait or lcd.buttonPressed(lcd.SELECT): 
    cls()
    lm(goodbye)
    lb(lcd.GREEN)
    sleep(1.5)
    break
  
  for button in buttons:
    if lcd.buttonPressed(button[0]):
      if button is not prev:
        cls()
        lb(button[1])
        lcd.message(button[2])
        prev = button
      break

cls()
lb(0)

