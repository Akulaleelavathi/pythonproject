import pytest
from settings.conftest import main_url
from settings.apirequest import postApi
from users.test_login import main_workspace

@pytest.fixture()
def test_get_productss():
    payload = {"searchKey":"","includeFacets":True,"includeDivisions":True,"includeCfas":True,"skuCode":"","sortDirection":"ASC","sortBy":"","inventoryFilter":"","stockFilter":"","divisionIds":[],"cfaIds":[],"statusFilter":"","collectionIds":[]}
    pageNo = 1
    pageSize = 10
    url = f"{main_url}/commerce-v2/products/search/{main_workspace['work_spaceId']}?pageNo={pageNo}&pageSize={pageSize}&customerId="
    # url="https://api-uat.beta.pharmconnect.com/commerce-v2/products/search/8ef5d569-3419-44e5-bb33-3ecfd260f796?pageNo=1&pageSize=20&customerId="
    response_data = postApi(url, payload)
    a_list=[]
    for i in response_data['products']:
        a_list.append (i["parentSku"])
    return a_list
    # print(a_list)

def test_skudata(test_get_productss):
    url = f"{main_url}/commerce-v2/products/search/{main_workspace['work_spaceId']}?pageNo=1&pageSize=20&customerId="
    payload = {"skuCode": test_get_productss[0]}

    # print(payload)
    response = postApi(url, payload)
    print(response)


