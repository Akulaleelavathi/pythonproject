import pytest

from settings.conftest import main_url
from settings.apirequest import getApi,postApi
from users.test_login import main_workspace
from test_schems import get_scheme
code = get_scheme()
@pytest.fixture
def test_response():
    url=f"{main_url}/commerce-v2/scheme/{main_workspace['work_spaceId']}/{code}"
    response=getApi(url)
    print(response)
    return (response["sku"][0])

def test_getdata(test_response):
    url = f"{main_url}/commerce-v2/products/search/{main_workspace['work_spaceId']}?pageNo=1&pageSize=10&customerId=your_customer_id_here"

    payload={"skuCode":test_response}
    response=postApi(url,payload)
    print(response)