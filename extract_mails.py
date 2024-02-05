import re
# [a-zA-Z0-9]+[\._-]?[a-zA-Z0-9]+@

data = input()

pattern = r"(^|(?<=\s))[a-zA-Z0-9]+[\._-]?[a-zA-Z0-9]+@[a-zA-Z]+\-?[a-zA-Z]+(\.[a-zA-Z]+\-?[a-zA-Z]+)+($|(?=\s))"

result = re.finditer(pattern, data)

for el in result:
    print(el.group())