N, L = map(int, input().split())
A = [list(map(lambda x: int(x == '-'), input().split('|'))) for _ in range(L)]
y = list(map(lambda x: int(x == 'o'), input()[::2])).index(1)

for ai in reversed(A):
    if ai[y]: y -= 1
    elif ai[y+1]: y += 1

ans = y+1

print(ans)