N = int(input())
XY = [list(map(int, input().split())) for _ in range(N)]
S = input()

lines = {}
for i in range(N):
    x, y = XY[i]
    d = S[i]
    
    if y not in lines: lines[y] = [0, 10**9]
    
    if d == 'L': lines[y][0] = max(lines[y][0], x)
    else: lines[y][1] = min(lines[y][1], x)
    
    if lines[y][0] > lines[y][1]:
        ans = 'Yes'
        break
else: ans = 'No'

print(ans)
