# 当data参数不为空的时候，urlopen（）提交方式为Post
import urllib.request
import urllib.parse

data = bytes(urllib.parse.urlencode({"word": "Hello"}), encoding="utf-8")
response = urllib.request.urlopen("http://httpbin.org/post", data=data)
print(response.read())
