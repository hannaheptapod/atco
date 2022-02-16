n = int(input())
a = list(map(int, input().split()))

s = set()
ans = 0

for ai in a:
    if ai not in s:
        s.add(ai)
        ans += 1

if len(s)%2 == 0: ans -= 1

print(ans)