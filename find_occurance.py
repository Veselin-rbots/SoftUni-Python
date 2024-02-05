import re

data = input()
serached = input()

pattern = f'\\searched\\b'

result = re.findall(pattern, data, re.IGNORECASE)

print(len(result))
