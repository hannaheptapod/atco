t = int(input())

for _ in range(t):
    a, s = map(int, input().split())

    if 2*a <= s: ans = 'Yes'
    else: ans = 'No'

    print(ans)