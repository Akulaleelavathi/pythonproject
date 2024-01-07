# import pytest
#
# from settings.conftest import main_url
# from settings.apirequest import postApi
# from users.test_login import main_workspace
#
# @pytest.fixture()
# def test_get_products():
#     payload = {}
#     url = f"{main_url}/commerce-v2/products/search/{main_workspace['work_spaceId']}?pageNo=1&pageSize=20&customerId="
#
#     response_data = postApi(url,payload)
#     # return(response_data)
#     for i in response_data['products']:
#         return (i['id'])
#
#
# def test_get_products2(test_get_products):
#     url="https://api-qa.beta.pharmconnect.com/commerce-v2/products/search/8ef5d569-3419-44e5-bb33-3ecfd260f796?pageNo=1&pageSize=10&customerId="
#     payload={"productVariantId":test_get_products}
#     response=postApi(url,payload)
#     print(response)






import pytest
from settings.conftest import main_url
from settings.apirequest import postApi
from users.test_login import main_workspace
from settings.auth_config import headers

import logging

logging.basicConfig(level=logging.DEBUG)

@pytest.fixture
def test_get_products():
    payload = {}
    url = f"{main_url}/commerce-v2/products/search/{main_workspace['work_spaceId']}?pageNo=1&pageSize=20&customerId="

    response_data = postApi(url, payload)
    ids_list = []
    for i in response_data["products"]:
        for j in i["productVariants"]:
            ids_list.append(j["productVariantId"])
    return ids_list

def test_get_products2(test_get_products):
    for product_id in test_get_products:
        base_url = f"{main_url}/commerce-v2/products/search/{main_workspace['work_spaceId']}?pageNo=1&pageSize=10&customerId="
        # url = base_url + str(product_id)
        payload = {"productVariantId": product_id}
         # print(payload)
        response = postApi(base_url, payload)
        print(response)



