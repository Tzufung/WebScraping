# 会话维持——一直保存cookie
import requests

# requests.get("http://httpbin.org/cookies/set/number/123")
# response = requests.get("http://httpbin.org/cookies")
# print(response.text)

s = requests.Session()
s.get("http://httpbin.org/cookies/set/number/123")
response = s.get("http://httpbin.org/cookies")
print(response.text)
