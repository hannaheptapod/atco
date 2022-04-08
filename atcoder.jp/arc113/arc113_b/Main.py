A, B, C = map(int, input().split())

if B%4 != 2 or C%2 == 0: bc = B**(2 - C%2) % 4
else: bc = 2 if C == 1 else 0

abc = A**bc % 10 if bc else A**4 % 10
print(abc)
