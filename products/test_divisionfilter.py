import pytest
from settings.conftest import main_url
from settings.apirequest import postApi
from users.test_login import main_workspace
from settings.auth_config import headers


##################SINGLE DIVISION VALUE############################


# @pytest.fixture()
# def test_get_products():
#     payload={}
#     pageNo = 1
#     pageSize = 20
#     url = f"{main_url}/commerce-v2/products/search/{main_workspace['work_spaceId']}?pageNo={pageNo}&pageSize={pageSize}&customerId="
#     response_data = postApi(url, payload)
#     # return(response_data)
#     for i in response_data["products"]:
#         for j in i["productVariants"]:
#             for k in j["division"]:
#                 a= (k["divisionId"])
#                 return a
#
# def test_division(test_get_products):
#     payload={"divisionIds":[test_get_products]}
#     base_url="https://api-qa.beta.pharmconnect.com/commerce-v2/products/search/8ef5d569-3419-44e5-bb33-3ecfd260f796?pageNo=1&pageSize=20&customerId="
#     response=postApi(base_url,payload)
#     print(response)


###################### ALL DIVISION AT A TIME###########################
@pytest.fixture()
def test_get_products():
    payload={}
    pageNo = 1
    pageSize = 20
    url = f"{main_url}/commerce-v2/products/search/{main_workspace['work_spaceId']}?pageNo={pageNo}&pageSize={pageSize}&customerId="
    response_data = postApi(url, payload)
    # return(response_data)
    ist_data=[]
    for i in response_data["products"]:
        for j in i["productVariants"]:
            for k in j["division"]:
                ist_data.append(k["divisionId"])
    a=set(ist_data)
    b=list(a)
    return a


def test_division(test_get_products):
    for division in test_get_products:
        payload={"divisionIds":[division]}
        pageNo = 1
        pageSize = 20 
        base_url=f"{main_url}/commerce-v2/products/search/{main_workspace['work_spaceId']}?pageNo={pageNo}&pageSize={pageSize}&customerId="
        response=postApi(base_url,payload)
        print(response)