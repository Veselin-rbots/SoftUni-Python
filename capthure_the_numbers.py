import re

line = input()
pattern = r"\d+"
numbers = []

while not line:
    match = re.findall(pattern, line)
    if match:
        numbers.extend(match)
    line = input()

print(*numbers, sep ="")
