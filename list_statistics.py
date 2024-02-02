n = int(input())

positives = []
negatives = []

for n in range(n):
    current_number = int(input())
    if current_number >= 0:
        positives.append(current_number)
    else:
        negatives.append(current_number)

print(positives)
print(negatives)

result = 0
for el in negatives:
    result += el

print(f"Count of positives: {len(positives)}." 
      f"Sum of negatives: {sum(negatives)}")