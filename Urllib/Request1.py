from urllib import request, parse

url = "http://httpbin.org/post"
headers = {"user-agent":
           "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.81 Safari/537.36",
           "Host": "httpbin.org"}
dic = {"name": "Tzufung"}
data = bytes(parse.urlencode(dic), encoding="utf-8")

req = request.Request(url=url, data=data, headers=headers, method='POST')
response = request.urlopen(req)
print(response.read().decode("utf-8"))
