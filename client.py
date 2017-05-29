#POC 

API_URL = 'http://app-prod-ws.meteoswiss.ch/v3/plzDetail2?plz=%s'
API_OVERVIEW_URL = 'http://app-prod-ws.meteoswiss.ch/v3/plzOverview2?plz=%s'

import requests
import json

url = API_URL % 8000
resp = requests.get(url)
data =  json.loads(resp.text)
