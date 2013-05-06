#!/usr/bin/python

# should have used post, just to lazy

import bottle
from bottle import request, route, template, view

@route('/message/<msg>', method='GET')
@view('main')
def message(msg):
  return dict(content=template("<p>Message set using [{{msg}}]</p>", msg=msg))

bottle.debug(True)
# listen on all interfaces
bottle.run(host='0.0.0.0', port=8080)  

