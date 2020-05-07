import sys
import json
import os

def handle(req):
    userInput = req
    print(os.environ)
    print(req)
    return json.dumps({"Chakeram ostad! 18 baba ... ": str(req)})
