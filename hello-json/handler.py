import sys
import json
import os

def handle(event, context):
    userInput = event.body
    username = event.headers
    return {
        "statusCode": 200,
        "body": {
            "heshmat" : userInput,
            "headers" : str(username)
        }
    }
