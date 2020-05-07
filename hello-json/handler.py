import sys
import json
import os

def handle(event, context):
    userInput = str(event.body)
    username = event.headers
    return {
        "statusCode": 200,
        "body": {
            "heshmat": userInput
        }
    }
