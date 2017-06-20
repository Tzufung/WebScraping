# urllib.parse.urlparse(urlstring, scheme="", allow_fragments=True)
# allow_fragments
from urllib.parse import urlparse

# result = urlparse("http://www.baidu.com/index.html;user?id=5#commnet", allow_fragments=False)
result = urlparse("http://www.baidu.com/index.html/#commnet", allow_fragments=False)
print(result)
