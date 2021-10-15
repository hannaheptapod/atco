h, w = map(int, input().split())
s = [input() for _ in range(h)]
ans = 'Yes'
for i in range(h):
    for j in range(w):
        if s[i][j] == '#':
            if i > 0 and s[i-1][j] == '#': continue
            elif i < h-1 and s[i+1][j] == '#': continue
            elif j > 0 and s[i][j-1] == '#': continue
            elif j < h-1 and s[i][j+1] == '#': continue
            else:
                ans = 'No'
                break
print(ans)