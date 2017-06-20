# 将保存的cookie填充到目标网站中
import http.cookiejar, urllib.request

cookie = http.cookiejar.LWPCookieJar()
cookie.load("cookie.txt", ignore_discard=True, ignore_expires=True)
handler = urllib.request.HTTPCookieProcessor(cookie)
opener = urllib.request.build_opener(handler)
response = opener.open("http://www.baidu.com")
print(response.read().decode("utf-8"))
