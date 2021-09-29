a, b, c = map(int, input().split())
sum = a + b
if a + c > sum:
    sum = a + c
if b + c > sum:
    sum = b + c
print(sum)