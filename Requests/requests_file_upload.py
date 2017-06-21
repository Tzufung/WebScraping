# 文件上传
import requests

files = {"file": open(r"C:\Users\DELL\Pictures\github.ico", "rb")}
response = requests.post("http://httpbin.org/post", files=files)
print(response.text)
