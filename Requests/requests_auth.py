# 认证设置
import requests
from requests.auth import HTTPBasicAuth
# r = requests.get("http://120.27.34.24:9001")
r = requests.get("http://120.27.34.24:9001", auth=HTTPBasicAuth("user", "123"))
# r = requests.get("http://120.27.34.24:9001", auth=("user", "123"))
print(r.status_code)
