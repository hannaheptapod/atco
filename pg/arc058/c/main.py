n, k = map(int, input().split())
d = list(input().split())

for i in range(n, 10**5):
    if all([di not in str(i) for di in d]): break

print(i)