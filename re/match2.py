import re

content = "Hello 1234567 World_This is a Regex Demo"

result = re.match("^Hello\s(\d+)\sWorld.*Demo$", content)
print(result)
print(result.group())
print(result.group(1))    # (\d+)

result2 = re.match("^He.*(\d+).*Demo$", content)
print(result2)
print(result2.group())
print(result2.group(1))    # 7, .*匹配尽可能多的，贪婪匹配

result3 = re.match("^He.*?(\d+).*Demo$", content)
print(result3.group(1))    # 1234567 .*?匹配尽可能少的，非贪婪匹配
