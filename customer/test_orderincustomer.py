from users.test_login import main_workspace
import pytest
from settings.conftest import main_url
from settings.apirequest import postApi,getApi



@pytest.fixture
def test_customerId():
    url=f"{main_url}/customers/{main_workspace['work_spaceId']}?includeCustomerGroupAssignments=1&includeWorkspaceMembers=1&pageNo=1&pageSize=20&includeOrderCount=1"
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





@pytest.fixture
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
    # print (response)
    # for i in response:
    #     print (len("orders"))
    data_list=[]
    for i in response["orders"]:
        data_list.append({"pofileId":i["pofileId"],"id":i["id"]})
        for k in i["orderLine"]:
            data_list.append({"ids":k["id"],"productVariantId":k["productVariantId"],"quantity":k["quantity"]})

    return data_list
    # print(data_list)








def test_deletedata(test_addtocard,test_customerId):
    test_delete= test_addtocard

    pofiledid=test_delete[0]["pofileId"]
    id=test_delete[0]["id"]
    orderline=test_delete[2]["ids"]
    print(pofiledid)
    print(id)
    print(orderline)
    payload={
    "sellerWorkspaceId":main_workspace["work_spaceId"],
    "customerId":  test_customerId[1],
    "importSource": "manual",
    "poFileId": pofiledid,
    "lines": [
        {
            "orderId": id,
            "orderLineId":orderline
        }
    ]
}

    url=f"{main_url}/commerce-v2/orders/deleteLines/{main_workspace['work_spaceId']}"
    response=postApi(url,payload)
    print(response)




def test_incresequntity(test_addtocard,test_customerId):
    increasequntity=test_addtocard
    pofiledid=increasequntity[0]["pofileId"]
    productvarientId=increasequntity[1]["productVariantId"]
    pofilelinedid=increasequntity[1]["ids"]
    quantity=increasequntity[1]["quantity"]
    print(pofiledid)
    print(productvarientId)
    print(pofilelinedid)
    print(quantity)




    payload={
    "customerId": test_customerId[1],
    "sellerWorkspaceId": main_workspace["work_spaceId"],
    "poFileId": pofiledid,
    "source": "manual",
    "lines": [
        {
            "productVariantId":productvarientId,
            "quantity": quantity*2,
            "operator": "add",
            "poFileLineId": pofilelinedid
        }
    ]
}

    url=f"{main_url}/commerce-v2/orders/additemtoactiveorder/{main_workspace['work_spaceId']}"
    response=postApi(url,payload)
    print(response)












def test_get_checkout(test_addtocard,test_customerId):
    payload={
    "sellerWorkspaceId": main_workspace["work_spaceId"],
    "customerId": test_customerId[0],
    "poFileIds": [
        "test_addtocard"
    ]
 }

    url=f"{main_url}/commerce-v2/orders/checkout/{main_workspace['work_spaceId']}"
    response=postApi(url,payload)
    print(response)


















