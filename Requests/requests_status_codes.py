# 状态码判断
import requests

response = requests.get("http://www.baidu.com")
exit() if not response.status_code == 200 else print("Request Successfully")
# exit() if not response.status_code == requests.codes.ok else print("Request Successfully")
