p = [i for i in [2]+list(range(3, 10**5 + 1, 2)) if all([i%j for j in range(3, int(i**0.5) + 1, 2)])]

a = [0]*(10**5 + 1)
for pi in p:
    if (pi+1)//2 in p: a[pi] = 1

b = [0]*(10**5 + 1)
sm = 0
for i in range(10**5 + 1):
    sm += a[i]
    b[i] = sm

q = int(input())

for _ in range(q):
    l, r = map(int, input().split())
    ans = b[r] - b[l-1]
    print(ans)