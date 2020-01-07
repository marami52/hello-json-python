import sys
import json

def handle(req):
    userInput = req
    return json.dumps({"Chakeram! baba ... ": userInput})
