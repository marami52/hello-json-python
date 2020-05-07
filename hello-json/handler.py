import sys
import json
import os

def handle(event, context):
    userInput = event.body
    username = event.headers['X_Consumer_Username']
    
    return {
        "statusCode": 200,
        "body": {
            "content-type-received": str(username)
        }
    }
