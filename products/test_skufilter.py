import pytest
from settings.conftest import main_url
from settings.apirequest import postApi
from users.test_login import main_workspace
from settings.auth_config import headers

@pytest.fixture()
def test_get_productss():
    payload = {}
    # url = f"{main_url}/commerce-v2/products/search/{main_workspace['work_spaceId']}?pageNo=41&pageSize=40&customerId="
    pageNo = 1
    pageSize = 20
    url = f"{main_url}/commerce-v2/products/search/{main_workspace['work_spaceId']}?pageNo={pageNo}&pageSize={pageSize}&customerId="
    response_data = postApi(url, payload)
    a_list=[]
    for i in response_data['products']:
        a_list.append (i["parentSku"])
    return a_list

def test_skudata(test_get_productss):
    url = "https://api-qa.beta.pharmconnect.com/commerce-v2/products/search/8ef5d569-3419-44e5-bb33-3ecfd260f796?pageNo=1&pageSize=20&customerId="
    payload = {"skuCode": test_get_productss[0]}

    # print(payload)
    response = postApi(url, payload)
    print(response)


