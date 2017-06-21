# 超时设置
import requests

response = requests.get("http://www.taobao.com", timeout=1)
print(response.status_code)
