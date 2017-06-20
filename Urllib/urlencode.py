from urllib.parse import urlencode

params = {"name": "Tzufung", "age": 22}
base_url = "http://www.baidu.com?"
url = base_url + urlencode(params)
print(url)
