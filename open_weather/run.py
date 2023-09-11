import requests
import json
import urllib.request
from pprint import pprint

API_KEY = "435d44089190098edf065f1097266562"

city = input("Enter a city name: ")
url = (
    f"https://api.openweathermap.org/data/2.5/weather?appid={API_KEY}&q={city}"
)

url_obj = urllib.request.urlopen(url)
data = url_obj.read()

json_bstr = url_obj.info().get_content_charset("utf-8")
json_str = data.decode(json_bstr)
query_result_json = json.loads(json_str)


pprint(query_result_json)

file_name = f"query_result_json_{city}"

with open(file_name, "w") as f:
    json.dump(query_result_json, f)
