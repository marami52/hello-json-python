import sys
import json
import os

def handle(event, context):
    userInput = str(event.body)
    username = event.headers['Http_X_Consumer_Username']
    return username
    #return json.dumps({"Chakeram ostad! 18 baba ... ": str(req)})
