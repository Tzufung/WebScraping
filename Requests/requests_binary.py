# 获取二进制数据——图片/视频
import requests

response = requests.get("http://github.com/favicon.ico")
with open(r"C:\Users\DELL\Pictures\github.ico", "wb") as f:
    f.write(response.content)
    f.close()

print(type(response.text), type(response.content))
print(response.text)
print(response.content)
