import urllib.request

response = urllib.request.urlopen("http://www.python.org")
print("The type of 'response' is: ", type(response))
print("status: ", response.status)
print("headers:  ", response.getheaders())
print("server: ", response.getheader("Server"))    # Not response.getheaders("Server")
print(response.read().decode("utf-8"))
