tail = input()
body = input()
head = input()

result = [head, body, tail]
result[0], result[2] = result[2] , result[0]
print(result)

