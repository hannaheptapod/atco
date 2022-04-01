N = int(input())
A = list(map(int, input().split()))
s = set(A)

for i in range(2001):
    if i not in s: break

print(i)
