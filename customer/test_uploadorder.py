
import requests
from users.test_login import main_workspace,main_token
import pytest
from settings.conftest import main_url
from settings.apirequest import postApi
# from settings.auth_config import headers
# from customer.test_orderincustomer import test_customerId

# cart_data = []
file_path = r"C:\Users\Lenovo\Downloads\RAJASTHAN DRUG HOUSE.xlsx"
@pytest.fixture
def test_upload():
    url =f"{main_url}/commerce-v2/poFile/upload/{main_workspace['work_spaceId']}?customerId=0938ed8d-09e0-42f3-af27-126d743b4e2b&importSource=upload&parserType=C2D_ORDER"

    payload={
    "customerId": "0938ed8d-09e0-42f3-af27-126d743b4e2b",
    "importSource": "upload",
    "parserType": "C2D_ORDER",
    }
    headers = {
        'Authorization': 'Bearer ' + f"{main_token}"

    }

    # Prepare file for upload
    files = {'file': open(file_path, 'rb')}

    response = requests.post(url, payload,headers=headers, files=files)
    mapped_data = []
    unmapped_data=[]
    for i in response.json():
        if i["status"] == "MAPPED":
            a = {"pvId": i["productVariantId"], "qty": i["quantity"], "PF_line_id": i["id"],"pf_id":i["poFileId"]}
            mapped_data.append(a)
        else:
            a = {"product_name": i["distributorProductName"],"pvId": i["productVariantId"], "qty": i["quantity"], "PF_line_id": i["id"],"pf_id":i["poFileId"]}
            unmapped_data.append(a)



    # print(mapped_data)
    # print(unmapped_data)

    empty_data = []
    for i in unmapped_data:
        payload = {
            "searchKey": i["product_name"]
        }
        url = "https://api-uat.beta.pharmconnect.com/commerce-v2/products/search/customer/8ef5d569-3419-44e5-bb33-3ecfd260f796?customerId=0938ed8d-09e0-42f3-af27-126d743b4e2b&pageNo=1&pageSize=20"
        response = postApi(url, payload)
        if response["total"] != 0:
            if i["data"]["qty"] == 0:
                a = {"pvId": response["products"][0]["productVariants"][0]["productVariantId"],
                     "qty": response["products"][0]["productVariants"][0]["minOrderQty"],
                     "PF_line_id": i["data"]["PF_line_id"], "pf_id": i["data"]["pf_id"]}
                mapped_data.append(a)
            else:
                a = {"pvId": response["products"][0]["productVariants"][0]["productVariantId"],
                     "qty": i["data"]["qty"],
                     "PF_line_id": i["data"]["PF_line_id"], "pf_id": i["data"]["pf_id"]}
                mapped_data.append(a)
        else:
            a = f'{i["product_name"]} not there in products'

            empty_data.append(a)
    # print(mapped_data)
#         # print(empty_data)
    return (mapped_data)
#         # return (empty_data)
#
#
#
@pytest.fixture
def test_add_card(test_upload):
    payload={

            "customerId": "0938ed8d-09e0-42f3-af27-126d743b4e2b",
            "sellerWorkspaceId": main_workspace["work_spaceId"],
            "source": "upload",
            "poFileId": test_upload[0]["pf_id"],
            "lines": [
                {
                    "productVariantId": i["pvId"],
                    "quantity": i["qty"],
                    "poFileLineId": i["PF_line_id"]
                }for i in test_upload
            ]



    }
    url=f"{main_url}/commerce-v2/orders/additemtoactiveorder/{main_workspace['work_spaceId']}"

    response=postApi(url,payload)
    print(response)
    return (response["orders"][0]["pofileId"])

































def test_checkout(test_add_card):
    payloaad={
    "sellerWorkspaceId": main_workspace["work_spaceId"],
    "customerId": "0938ed8d-09e0-42f3-af27-126d743b4e2b",
    "poFileIds": [test_add_card]


}
    url=f"{main_url}/commerce-v2/orders/checkout/{main_workspace['work_spaceId']}"
    response=postApi(url,payloaad)
    print(response)
