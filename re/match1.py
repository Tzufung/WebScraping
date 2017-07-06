# 常规匹配

import re

content = "Hello 123 4567 World_This is a Regex Demo"
result = re.match("Hello", content)
print(result)
print(result.group())
