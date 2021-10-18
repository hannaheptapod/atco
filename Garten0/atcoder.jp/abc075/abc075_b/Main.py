h, w = map(int, input().split())
s = [input() for _ in range(h)]
lst = [[0 for _ in range(w+2)] for _ in range(h+2)]
for i in range(1, h+1):
    for j in range(1, w+1):
        if s[i-1][j-1] == '#':
            for ii in range(i-1, i+2):
                for jj in range(j-1, j+2): lst[ii][jj] += 1
ans = [str() for _ in range(h)]
for i in range(1, h+1):
    for j in range(1, w+1):
        if s[i-1][j-1] == '#': ans[i-1] += '#'
        else:  ans[i-1] += str(lst[i][j])
_ = [print(a) for a in ans]