# 设置过短的响应时间，导致异常
import urllib.request
import urllib.error
import socket

try:
    response = urllib.request.urlopen("http://httpbin.org/get", timeout=0.1)
except urllib.error.URLError as e:
    if isinstance(e.reason, socket.timeout):
        print("TIME OUT")
