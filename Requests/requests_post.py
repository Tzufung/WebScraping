# 基本post请求——form data
import requests

data = {"name": "Tzufung", "age": "25"}
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36 Edge/15.15063"
}

response = requests.post("http://httpbin.org/post", data=data, headers=headers)
print(response.text)
print(response.json())
