# Make a Request
# 文件名不要与库名冲突：取名requests.py时，pycharm报错
import requests

response = requests.get("https://www.baidu.com")
print("Type of response: ", type(response))
print("Status_code: ", response.status_code)
print("Type of response.text: ", type(response.text))
print("Response.text: ", response.text)
print("Cookies: ", response.cookies)

requests.post("http://httpbin.org/post", data={"key": "value"})
requests.put("http://httpbin.org/put", data={"key": "value"})
requests.delete("http://httpbin.org/delete")
requests.head("http://httpbin.org/head")
requests.options("http://httpbin.org/get")
