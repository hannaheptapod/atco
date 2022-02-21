N = int(input())
a = [int(input()) for _ in range(N)]

if any([ai%2 for ai in a]): ans = 'first'
else: ans = 'second'

print(ans)