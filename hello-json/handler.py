import sys
import json
import requests

def handle(req):
    headers = {}
    request = requests.Request('GET', 'http://gateway.openfaas:8080/function/list-functions/?user=marami52', headers=headers)
    prepped = request.prepare()
    with requests.Session() as session:
        response = session.send(prepped)
    userInput = req
    return response.text
    #return json.dumps({"Chakeram ostad! 11baba ... ": userInput})
