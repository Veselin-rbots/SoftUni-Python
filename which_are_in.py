substrings = input().split(", ")
words = input().split(", ")

result = [subst for subst in substrings for word in words  if subst in word]
# unique = list(set[result])

# [el for el in result if result.count(el) == 1]
# for word in words:
#     for substr in substrings:
#         if substr in word and substr not in result:
#             result.append(substr)
print(result)
print(sorted(set(result), key=result.index))
