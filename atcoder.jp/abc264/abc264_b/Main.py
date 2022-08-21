R, C = map(int, input().split())

r, c = min(R, 16-R), min(C, 16-C)

ans = 'black' if min(r, c)%2 else 'white'

print(ans)
