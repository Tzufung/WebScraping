# urllib.parse.urlparse(urlstring, scheme="", allow_fragments=True)
# urlstring
from urllib.parse import urlparse

result = urlparse("http://www.baidu.com/index.html;user?id=5#commnet")
print(type(result), result)
