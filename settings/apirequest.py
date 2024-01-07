import requests
from users.test_login import main_token

headers = {
    "Content-Type": "application/json",
    "Authorization": "Bearer "+f"{main_token}"
}
def getApi(url):
    response = requests.get(url,headers = headers)
    return response.json()

def postApi(url,payload):
    response = requests.post(url,json=payload,headers = headers)
    return response.json()

def putApi(url,payload):
    response = requests.put(url, json=payload, headers = headers)
    return response.json()

def deleteApi(url, payload):
    response = requests.delete(url, json= payload, headers = headers)
    return response.json()