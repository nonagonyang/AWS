import urllib3
import json

def lambda_handler(event, context):
    http = urllib3.PoolManager()
    response = http.request('GET', 'https://api.quotable.io/random?tags=humor')
    body=json.loads(response.data)["content"]
    return body
    