# 获取cookie
import requests

response = requests.get("http://www.baidu.com")
print(response.cookies)
print(response.cookies.items())
for key, value in response.cookies.items():
    print(key + "=" + value)
