import sys
import json
import os

def handle(req):
    userInput = req
    print(os.environ)
    return json.dumps({"Chakeram ostad! 17 baba ... ": userInput})
