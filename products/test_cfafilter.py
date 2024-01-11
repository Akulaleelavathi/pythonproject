import pytest
from settings.conftest import main_url
from settings.apirequest import postApi
from users.test_login import main_workspace


@pytest.fixture
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
            for k in j["cfas"]:
                ist_data.append(str(k["cfaId"]))
    a= set(ist_data)
    b = list(a)
    return b

def test_cfas(test_get_products):
    for cfas in test_get_products:
        payload={"cfaIds":[cfas]}
        # print(payload)
        pageNo = 1
        pageSize = 20
        base_url=f"{main_url}/commerce-v2/products/search/{main_workspace['work_spaceId']}?pageNo={pageNo}&pageSize={pageSize}&customerId="
        # base_url="https://api-qa.beta.pharmconnect.com/commerce-v2/products/search/8ef5d569-3419-44e5-bb33-3ecfd260f796?pageNo=1&pageSize=20&customerId="
        response=postApi(base_url,payload)
        print(response)
        print(len(test_get_products))