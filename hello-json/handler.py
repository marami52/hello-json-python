import sys
import json
import os

def handle(event, context):
    userInput = event.body
    username = event.headers['X_Consumer_Username']
    return json.dumps({"abc" : str(username)})
