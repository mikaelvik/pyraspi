#!/usr/bin/python

# should have used post, just to lazy

import bottle
from bottle import request, route, template

from CharLCDPlate import CharLCDPlate

l = CharLCDPlate()

@route('/backlight/<bg>', method='GET')
def backlight(bg):
  l.backlight(
    bg.isdigit() and int(bg) or eval('l.' + bg.upper())
  )
  return template("<p>Backlight set using [{{bg}}]</P>", bg=bg)

@route('/message/<msg>', method='GET')
def message(msg):
  l.clear()
  l.message(msg)
  return template("<p>Message set using [{{msg}}]</P>", msg=msg)

@route('/message/slideleft/<msg>', method='GET')
def message_slidein(msg):
  l.messageSlideLeft(msg=msg)
  return template("<p>Message slided left using [{{msg}}]</P>", msg=msg)

bottle.debug(True)
# listen on all interfaces
bottle.run(host='0.0.0.0', port=80)  

