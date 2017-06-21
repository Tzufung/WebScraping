# 证书验证
import requests

# response = requests.get("https://www.12306.cn")
# requests.exceptions.SSLError: [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed (_ssl.c:749)
# response = requests.get("https://www.12306.cn", verify=False)
response = requests.get("https://www.12306.cn", cert=("证书路径"))    # 导入本地证书
print(response.status_code)
