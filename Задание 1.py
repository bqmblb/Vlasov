#задание 1
abcd = [c for c in input()]
abcd[0], abcd[1] = abcd[1], abcd[0]
print(*abcd, sep='')