n = int(input())
even_nums = []
odd_nums = []
negative_nums =[]
positive_nums = []

for iteration in range(n):
    current_number = int(input())
    if current_number % 2 == 0:
        even_nums.append(current_number)
    if not current_number % 2 == 0:
        odd_nums.append(current_number)
    if current_number >= 0:
        positive_nums.append(current_number)
    else:
        negative_nums.append(current_number)

print(f"Count of positives: {positive_nums}. Sum of negatives: {negative_nums}.")
print(f"Count of odd nums: {odd_nums}. Sum of even nums: {even_nums}.")