import re

content = "Extra string Hello 1234567 World_This is a Regex Demo"

result = re.match("Hello.*?(\d+).*?Demo", content)
print(result)

result1 = re.search("Hello.*?(\d+).*?Demo", content)
print(result1.group(1))
