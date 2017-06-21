# 添加headers模拟浏览器登陆
import requests

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36 Edge/15.15063"
}
response = requests.get("http://www.zhihu.com", headers=headers)
# response = requests.get("http://www.zhihu.com")    # <html><body><h1>500 Server Error</h1>
print(response.text)

