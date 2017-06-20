import urllib.request

request = urllib.request.Request("http://python.org")
response = urllib.request.urlopen(request)
print(response.read().decode("utf-8"))
