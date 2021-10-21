n, m = map(int, input().split())
ans = [0]*n
for _ in range(m):
    a, b = map(int, input().split())
    ans[a-1] += 1
    ans[b-1] += 1
_ = [print(ai) for ai in ans]