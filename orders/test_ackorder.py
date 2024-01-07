from users.test_login import main_workspace
import pytest
from settings.conftest import main_url
from settings.apirequest import postApi,getApi


@pytest.fixture
def test_allcustomers():
    payload = {
        "workspaceId":main_workspace['work_spaceId'],
        "customerId": "",
        "pageNo": 1,
        "pageSize": 20,
        "sortBy": "orderPlacedAt",
        "sortDirection": "DESC",
        "includeSummary": True,
        "includeInvoice": True,
        "includeCustomer": True,
        "includeStatus": True,
        "includeCFA": True,
        "includeDivision": True,
        "searchKeyword": "",
        "startDate": "2023-12-29",
        "endDate": "2024-01-05",
        "filterModel": {
            "headDivisionIds": [],
            "divisionIds": [],
            "cfaIds": [],
            "status": [],
            "customerIds": []
        },
        "skip": 1
    }
    url = f"{main_url}/commerce-v2/orders?workspaceId={main_workspace['work_spaceId']}"

    response = postApi(url, payload)
    data_list=[]

    # Extract unique order IDs and customer IDs for orders with status "SubmittedByCustomer"


    for i in response["order"]:
        if i["status"] == "SubmittedByCustomer":
            data_list.append({"orderId": i["id"], "customerId": i["customerId"]})


    return data_list
    # return (submitted_orders_info)






@pytest.fixture
def test_customersingle(test_allcustomers):
    submitted_orders_info = test_allcustomers

    # Extract customer ID from the first submitted order
    customer_id = submitted_orders_info[0]["customerId"]
    order_id = submitted_orders_info[0]["orderId"]
    print(customer_id)
    print(order_id)

    payload = {
        "filter": {
            "divisionIds": []
        },
        "searchKey": "",
        "includeInvoice": True,
        "includeTax": True,
        "includeCustomer": True,
        "includePromotions": True,
        "sortDirection": "DESC",
        "sortBy": "",
        "customerId": customer_id,
    }

    url = f"{main_url}/commerce-v2/orders/details/{main_workspace['work_spaceId']}/{order_id}?includeInvoice=true"

    # Now you can make your API request using the constructed URL and payload
    response = postApi(url, payload)
    # print(response)
    # print(len(response))
    for key in response:
        if key == "id":
            return(response[key])










def test_approvereq(test_customersingle):
    payload=[
    {
        "orderId": test_customersingle,
        "status": "Approved"
    }

]
    url=f"{main_url}/commerce-v2/orders/{main_workspace['work_spaceId']}"
    response=postApi(url,payload)
    print(response)