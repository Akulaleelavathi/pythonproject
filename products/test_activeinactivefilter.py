import pytest
from settings.conftest import main_url
from settings.apirequest import postApi
from users.test_login import main_workspace
from settings.auth_config import headers
@pytest.fixture()
def test_get_products():
    payload={}
    pageNo = 1
    pageSize = 20
    url = f"{main_url}/commerce-v2/products/search/{main_workspace['work_spaceId']}?pageNo={pageNo}&pageSize={pageSize}&customerId="
    response_data = postApi(url, payload)
    return (response_data)

def test_activiinactive(test_get_products):
        payload={"statusFilter":"ACTIVE"}
        pageNo = 1
        pageSize = 40
        base_url=f"{main_url}/commerce-v2/products/search/{main_workspace['work_spaceId']}?pageNo={pageNo}&pageSize={pageSize}&customerId="

        response = postApi(base_url, payload)
        print(response)



