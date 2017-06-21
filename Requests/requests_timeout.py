# 超时设置
import requests
from requests.exceptions import ReadTimeout

try:
    response = requests.get("http://www.taobao.com", timeout=0.001)
    print(response.status_code)
except ReadTimeout:
    print("Timeout")
