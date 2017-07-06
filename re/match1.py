# 常规匹配

import re

content = "Hello 123 4567 World_This is a Regex Demo"

result = re.match("Hello", content)
print(result)
print(result.group())

result2 = re.match("^Hello\s\d\d\d\s\d{4}\s\w{10}.*Demo$", content)
print(result2)
print(result2.group())

result3 = re.match("^Hello.*Demo$", content)
print(result3)
print(result3.group())
