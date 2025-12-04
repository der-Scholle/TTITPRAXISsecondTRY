nums = [1, 2, 3, 4]
duplicate = False

for i in range(len(nums)):
    for j in range(i + 1, len(nums)):
        if nums[i] == nums[j]:
            duplicate = True
            break

print(duplicate)

nums = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]
duplicate = False

for i in range(len(nums)):
    for j in range(i + 1, len(nums)):
        if nums[i] == nums[j]:
            duplicate = True
            break

print(duplicate)

nums = [1, 2, 3, 1]
duplicate = False

for i in range(len(nums)):
    for j in range(i + 1, len(nums)):
        if nums[i] == nums[j]:
            duplicate = True
            break

print(duplicate)