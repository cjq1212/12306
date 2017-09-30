import re
import requests
import certifi
import urllib3
from pprint import pprint

urllib3.disable_warnings ()
url = 'https://kyfw.12306.cn/otn/resources/js/framework/station_name.js?station_version=1.9026'
response = requests.get (url, verify=False)
stations = re.findall (u'([\u4e00-\u9fa5]+)\|([A-Z]+)', response.text)
pprint (dict (stations), indent=4)
