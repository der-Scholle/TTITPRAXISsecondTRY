j = "ab"
s = "aabbccd"

count = 0

for ch in s:
    if ch in j:
        count += 1

print(count)