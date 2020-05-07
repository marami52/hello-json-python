import sys
import json
import os

def handle(event, context):
    userInput = event.body
    username = event.headers
    return json.dumps({username})
