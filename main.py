#スクレイピング
from pprint import pprint
import requests

# url = "https://tech-diary.net"
# r = requests.get(url)
# print(r.text)
#API

url = "https://coincheck.com/api/ticker"
r = requests.get(url)
#pprint(r.json())

d_dict = {}
d_dict = r.json

pprint(d_dict)