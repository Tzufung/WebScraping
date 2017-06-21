# response 属性
import requests

response = requests.get("http://www.jianshu.com")
print(type(response.status_code), response.status_code)
print(type(response.headers),response.headers)
print(type(response.url), response.url)
print(type(response.cookies), response.cookies)
print(type(response.history), response.history)
