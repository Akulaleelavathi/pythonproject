from settings.conftest import main_url
from settings.apirequest import getApi,postApi
from users.test_login import main_workspace


def get_scheme():
    url = f"{main_url}/commerce-v2/scheme/{main_workspace['work_spaceId']}?pageNo=1&pageSize=20&skuCode=&sortDirection=&sortBy=&includeCFA=true&startDate=2023-12-03&endDate=2024-01-02&dispatchFilters=true&status=&promotionType="

    payload={}
    response=postApi(url,payload)
    # print(response)
    # return response
    for i in response["promotions"]:
        return i['id']

