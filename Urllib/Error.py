from urllib import request, error

try:
    response = request.urlopen("http://www.baiduyixa.com")
except error.HTTPError as e:
    print(e.reason, e.code, e.headers, sep="\n")
except error.URLError as e:
    print(e.reason)
else:
    print("Request Successfully")
