from flask_ask import Ask, statement, convert_errors
from flask import Flask,jsonify
from flask_cors import CORS, cross_origin
import os
import logging
import time

app = Flask(__name__)
ask = Ask(app, '/')

logging.getLogger("flask_ask").setLevel(logging.DEBUG)

state = False
timer = 0

@ask.intent('StudyMode', mapping={'status': 'status'})
def script_execution(status):

    if status in ['on','high' ]:
      if (state == True):
        return statement('StudyMode is already on')
      else:
        os.system('pihole enable')
        global timer
	timer = int(time.time()) + 60*5
        global state
        state = True
        return statement('Turning StudyMode {}'.format(status))

    if status in ['off','low' ]:
      if (state == False):
        return statement('StudyMode is already off')
      elif(time.time() < timer):
	global timer
	minsLeft = (timer - int(time.time()))/60
	return statement('Remaing time on StudyMode is ' + str(minsLeft) + ' minutes' )
      else:
        os.system('pihole disable')
        global state
        state = False;
        return statement('Turning StudyMode{}'.format(status))

if __name__ == '__main__':
  port = 5000
  app.run(host='0.0.0.0', port=port)
