S = input()
T = int(input())

x, y, k = 0, 0, 0
for si in S:
    if si == 'L': x -= 1
    elif si == 'R': x += 1
    elif si == 'U': y += 1
    elif si == 'D': y -= 1
    else: k += 1

if T == 1: ans = abs(x) + abs(y) + k
else: ans = max(abs(x) + abs(y) - k, (abs(x) + abs(y) - k)%2)

print(ans)