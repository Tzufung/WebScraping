import re

# content = "Hello 1234567 World_This " \
#           "is a Regex Demo"

content = """Hello 1234567 World_This
is a Regex Demo"""

result = re.match("^He.*?(\d+).*Demo$", content)
print(result)    # None .无法匹配换行符

result1 = re.match("^He.*?(\d+).*Demo$", content, re.S)
print(result1)
print(result1.group(1))
