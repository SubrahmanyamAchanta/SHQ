"""
Task 11
Use https://api.nasa.gov/ Insight( https://mars.nasa.gov/insight/weather/)
Display the current weather on Mars in browser.

The API given in the question is not giving correct weather information currently. Still, I completed this task with the
available information to show that I know how to parse json and display it on graphs.
"""

import json
import requests
import webbrowser
from urllib.parse import urlencode

BASE_URL = 'https://quickchart.io/chart?%s'
REQ_URL = 'https://api.nasa.gov/insight_weather/?api_key=KfmbiLTrQC9kU44pcP8Uje8XRBibbqlYbVw4UbQv&feedtype=json&ver' \
           '=1.0'
IMG_URL = 'https://mars.nasa.gov/layout/embed/image/insightweather/'

response = requests.get(REQ_URL)
data = json.loads(response.text)

config = {
  "type": "bar",
  "data": {
    "labels": ['AT', 'HWS', 'PRE', 'WD'],
    "datasets": [{
      "label": 'AT',
      "data": data["validity_checks"]["1219"]["AT"]["sol_hours_with_data"]
    }, {
      "label": 'HWS',
      "data": data["validity_checks"]["1219"]["HWS"]["sol_hours_with_data"]
    }, {
      "label": 'PRE',
      "data": data["validity_checks"]["1219"]["PRE"]["sol_hours_with_data"]
    }, {
      "label": 'WD',
      "data": data["validity_checks"]["1219"]["WD"]["sol_hours_with_data"]
    }]
  }
}

params = {
    'chart': json.dumps(config),
    'width': 500,
    'height': 300,
    'backgroundColor': 'white',
}

url = BASE_URL % urlencode(params)
webbrowser.open(url, new=1)
# another URL available on NASA website which provides weather information as a picture.
webbrowser.open(IMG_URL)
