# 代理设置
import requests

proxies = {
    "http": "218.3.131.244:808",
    "https": "1.195.8.235"
}

# proxies = {"http": "http://user:password@127.0.0.1:9743"}
# pip3 install "requests[socks]"
# proxies = {"http": "socks5://user:password@127.0.0.1:9743"}

response = requests.get("http://www.taobao.com", proxies=proxies)
print(response.status_code)
