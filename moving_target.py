targets = input().split()
# print(targets)
# targets = [int(target) for target in targets]
targets = list(map(int, targets))
# print(targets)

data = input()


def shoot(nums, i, v):
    a = 5
    if 0 <= i < len(nums):
        nums[i] -= v
        if nums[i] <= 0:
            nums.pop(i)
    return nums

def add_target(nums, i, v):
    if 0 <= i < len(nums):
       nums.insert(i, v)
    else:
        print("Invalid placement!")
    return nums

def strike(nums, i ,v):
    left_index = i - v
    right_index = i + v

    if left_index >= 0 and right_index < len(nums):
        left_part = nums[:left_index]
        right_part = nums[:right_index]
        nums = left_part + right_part
    else:
        print("Strike missed!")

while not data == "End":
    command, index, value = data.split()
    index = int(index)
    value = int(index)
    # strike = int(index)

    if command == "shoot":
        targets = shoot(targets, index, value)
    elif command == "Add":
        targets = add_target(targets, index, value)
    elif command == "Strike":
        targets = strike(targets, index, value)

    data = input()

print('|'.join(map(str, targets)))

# [str(el) for el in targets]