from flask import Flask
from flask_ask import Ask, statement, convert_errors
import os
import logging

app = Flask(__name__)
ask = Ask(app, '/')

logging.getLogger("flask_ask").setLevel(logging.DEBUG)

state = False;

@ask.intent('StudyMode', mapping={'status': 'status'})
def script_execution(status):

    if status in ['on','high' ]:
      if (state == True):
        return statement('StudyMode is already on')
      else:
        os.system('pihole enable')
        global state 
        state = True;
        return statement('Turning StudyMode {}'.format(status))
        

    if status in ['off','low' ]:
      #print('status of mode',state)
      if (state == False):
        return statement('StudyMode is already off')
      else:
        os.system('pihole disable')
        global state
        state = False;
        return statement('Turning StudyMode{}'.format(status))

if __name__ == '__main__':
  port = 5000 
  app.run(host='0.0.0.0', port=port)
