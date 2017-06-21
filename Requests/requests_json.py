# 解析json
import requests
import json

response = requests.get("http://httpbin.org/get")
print(response)
print(type(response.text))
print(response.json())
print(json.loads(response.text))
print(type(response.json()))
