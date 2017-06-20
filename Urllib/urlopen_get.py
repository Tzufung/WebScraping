# 利用GET方式请求百度
import urllib.request

response = urllib.request.urlopen("http://www.baidu.com")
print(response.read().decode("utf-8"))
