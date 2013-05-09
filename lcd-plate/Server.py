#!/usr/bin/python

# should have used post, just to lazy

import bottle
from bottle import request as req, template, view
from bottle import static_file
from bottle import get, post

from CharLCDPlate import CharLCDPlate

l = CharLCDPlate()

@get('/static/<filename>')
def static_content(filename):
  return static_file(root='static/', filename=filename)

@get('/lcd')
@post('/lcd')
@view('main')
def lcd_get():
  params = req.method == 'GET' and req.query or req.forms
  content = ''
  if params.msg: content += message(params.msg)
  if params.bg:  content += backlight(params.bg)
  return dict(content=content)

@get('/backlight')
@get('/backlight/<bg>')
def backlight(bg='off'):
  l.backlight(
    bg.isdigit() and int(bg) or eval('l.' + bg.upper())
  )
  return template("<p>Backlight: [{{bg}}]</P>", bg=bg)

@get('/message')
@get('/message/<msg>')
def message(msg=""):
  l.clear()
  l.message(msg)
  return template("<p>Message: [{{msg}}]</P>", msg=msg)

bottle.debug(True)
# listen on all interfaces
bottle.run(
  host='0.0.0.0', 
  port=80,
  reloader=True
)  

