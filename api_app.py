import requests
import os

client_id = os.environ.get('CLIENT_ID')
api_key = os.environ.get('API_KEY')

uri = 'https://api.yelp.com/v3'

headers = {
    "Authorization": f"Bearer {api_key}",
}

# biz_search = requests.get(
#     url=uri + '/businesses/search',
#     params={
#         "location": "San Diego, CA",
#         "categories": "restaurants"
#     },
#     headers=headers
# )

biz_detail_search = requests.get(
    url = uri + '/businesses/cucina-urbana-san-diego-4',
    # params={"business_id_or_alias": ""},
    headers=headers
)

print('debug')
