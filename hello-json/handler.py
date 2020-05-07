import sys
import json
import os

def handle(req):
    userInput = req
    a = os.environ['Http_X_Consumer_Username']
    return json.dumps({"Chakeram ostad! 17 baba ... ": str(a)})
