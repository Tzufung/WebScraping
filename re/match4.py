import re

content = "prince is $5.00"

result = re.match("prince is $5.00", content)
print(result)

result1 = re.match("prince is \$5\.00", content)
print(result1)
