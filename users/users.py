import requests
workspaces = ""

def send_otp(main_url,mobile_number):
    payload = {
        "authChannel": "mobile",
        "mobile": "091" + f"{mobile_number}"
    }
    response = requests.post(main_url+"/sendotp", json = payload)
    #print(response.json(), '==============================>sendotp response')
    return response.json()

def verify_otp(test_send_otp,main_url,mobile_number):
    payload = {
        "authChannel": "mobile",
        "mobile": "091"+f"{mobile_number}",
        "otp": str(test_send_otp['mobile']['otp'])
    }
    headers = {
        "Content-Type": "application/json",
        "Authorization": "Bearer " + f"{test_send_otp['temptoken']}"
    }

    #print(test_send_otp["mobile"]["otp"], '==============================> otp value from send otp')
    response = requests.post(main_url+"/verifyotp",json = payload,headers = headers)
    #print(response.json(), '=========================================> verify otp response')
    return response.json()["token"]


def get_workspace(test_verify_otp,main_url):
    headers = {
        "Content-Type": "application/json",
        "Authorization": "Bearer "+f"{test_verify_otp}"
    }

    response = requests.get(main_url+"/workspaces",headers=headers)
    for i in response.json():
        each_cfa= {"work_spaceId":i["id"]}
        workspaces=each_cfa

    return workspaces