N = int(input())
A = sorted(map(int, input().split()))
for i in range(1, N):
    d = A[i]-A[0]
    if d: break

if d == 0: ans = 1
elif N == 2: ans = 2 if d == 1 else 1
else:
    ans = len(set(ai%2 for ai in A))

    if ans == 2:
        for x in range(2, int(d**0.5)+1):
            if ans == 1: break
            if d%x == 0: ans = min([ans, len(set(ai%x for ai in A)),
                                   len(set(ai%(d//x) for ai in A))])
        else: ans = min(ans, len(set(ai%d for ai in A)))

print(ans)
