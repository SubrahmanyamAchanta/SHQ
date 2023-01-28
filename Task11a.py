"""
Task 11
Use https://quickchart.io/
Build a bar graph to display 5 fields inputted by the user and display the output in browser.
"""

import json
import webbrowser
from urllib.parse import urlencode

BASE_URL = 'https://quickchart.io/chart?%s'
input_labels = input("Please enter 5 labels comma separated without spaces. : ").split(',')
user_data = input("Please enter 5 data values comma separated without spaces. : ").split(',')

config = {
    "type": "bar",
    "data": {
        "labels": input_labels,
        "datasets": [{
            "label": "Score",
            "data": user_data
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
