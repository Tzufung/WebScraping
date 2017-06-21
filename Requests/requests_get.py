import requests

data = {"name": "Tzufung", "age": "25"}
response = requests.get("http://httpbin.org/get", params=data)
# response = requests.get("http://httpbin.org/get?name=Tzufung&age=25")
print(response.text)
