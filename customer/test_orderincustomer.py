from users.test_login import main_workspace
import pytest
from settings.conftest import main_url
from settings.apirequest import postApi,getApi



@pytest.fixture
def test_customerId():
    url="https://api-qa.beta.pharmconnect.com/customers/8ef5d569-3419-44e5-bb33-3ecfd260f796?includeCustomerGroupAssignments=1&includeWorkspaceMembers=1&pageNo=1&pageSize=20&includeOrderCount=1"
    response=getApi(url)
    list=[]
    for i in response["customers"]:
        list.append(i["id"])
    return (list)




@pytest.fixture
def test_get_products(test_customerId):
    payload={}
    url=f"{main_url}/commerce-v2/products/search/customer/{main_workspace['work_spaceId']}?pageNo=1&pageSize=7&customerId={test_customerId[1]}"
    response=postApi(url,payload)
    # print(response)
    list=[]
    for i in response["products"]:
        for j in i["productVariants"]:

            list.append ({"productId":j["productVariantId"],"minquty":j["minOrderQty"]})


    return(list)
    # print(list)





# @pytest.fixture
def test_addtocard(test_get_products,test_customerId):
    payload={
    "customerId": test_customerId[1],
    "sellerWorkspaceId":main_workspace["work_spaceId"],
    "source": "manual",
    "lines": [
        {
            "productVariantId": i["productId"],
            "quantity":i["minquty"],
            "operator": "add"
        }for i in test_get_products
    ]
    }
    url=f"{main_url}/commerce-v2/orders/additemtoactiveorder/{main_workspace['work_spaceId']}"
    response = postApi(url, payload)
    print (response)
    # for i in response:
    #     print (len("orders"))

    for i in response["orders"]:
        print(i["pofileId"],i["id"])










# def test_get_checkout(test_addtocard,test_customerId):
#     payload={
#     "sellerWorkspaceId": main_workspace["work_spaceId"],
#     "customerId": test_customerId[0],
#     "poFileIds": [
#         "test_addtocard"
#     ]
#  }
#
#     url=f"{main_url}/commerce-v2/orders/checkout/{main_workspace['work_spaceId']}"
#     response=postApi(url,payload)
#     print(response)


















