#!/usr/bin/python

import bottle
from bottle import get, static_file

import os
from datetime import datetime

effects = [
  'none', 'negative', 'solarise', 'sketch',
  'denoise', 'emboss', 'oilpaint', 'hatch', 
  'gpen', 'pastel', 'watercolour', 'film', 
  'blur', 'saturation', 'colourswap', 'wash'
]
effect = effects[0]

@get('/images/<filename>')
def images(filename):
  return static_file(root='images/', filename=filename)

@get("/now")
def capture_now():
  filename = 'now-%s.png' % (datetime.now().strftime("%Y%m%d%H%M%S"), )
  os.system("raspistill -o images/%s -n -br 55 -t 100 -q 70 -h 600 -w 900 -ifx %s" % (filename, effect))
  return images(filename)

bottle.debug(True)
# listen on all interfaces
bottle.run(
  host='0.0.0.0', 
  port=80,
  reloader=True
)  

