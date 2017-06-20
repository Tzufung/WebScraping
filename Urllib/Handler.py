import urllib.request

proxy_handler = urllib.request.ProxyHandler({
    "http": "http://183.159.196.77",
    "https": "https://119.7.79.220"
})
# urllib.request.ProxyHandler(proxies=None)
# If proxies is given, it must be a dictionary mapping protocol names to URLs of proxies.

opener = urllib.request.build_opener(proxy_handler)
# urllib.request.build_opener([handler, ...])
# Return an OpenerDirector instance, which chains the handlers in the order given.

response = opener.open("http://baidu.com")
print(response.read())
