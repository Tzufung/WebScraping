# urllib.parse.urlparse(urlstring, scheme="", allow_fragments=True)
# scheme
from urllib.parse import urlparse

# result = urlparse("www.baidu.com/index.html;user?id=5#commnet", scheme="https")
result = urlparse("http://www.baidu.com/index.html;user?id=5#commnet", scheme="https")
print(result)
