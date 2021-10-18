n = int(input())
k = 0
while n > 1:
  n >>= 1
  k += 1
print(k)