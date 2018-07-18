import json
import requests
import os

client_secret = os.environ['SO_CLIENT_SECRET']

url = 'https://api.stackexchange.com'
search_endpoint = '/2.2/search?'
site = 'site=stackoverflow'
intitle = 'intitle=Hello World'

final_url = url + search_endpoint + intitle + '&' + site
response = requests.get(final_url)

data = json.loads(response.content)

print(json.dumps(data, indent=4, sort_keys=True))
