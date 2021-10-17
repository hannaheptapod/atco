n, q = map(int, input().split())
s = input()
dp = [[0]*n for _ in range(n)]
dp[0][0] = int(s[0] == '(') - int(s[0] == ')')
for j in range(1, n):
    dp[0][j] = dp[0][j-1] + int(s[j] == '(') - int(s[j] == ')')
for i in range(1, n):
    for j in range(i, n):
        dp[i][j] = dp[i-1][j] - (int(s[i-1] == '(') - int(s[i-1] == ')'))
pl = [0]*n
for _ in range(q):
    qi, l, r = map(int, input().split())
    if qi == 1:
        if s[l-1] == '(' and s[r-1] == ')':
            pl[l-1] -= 2
            pl[r-1] += 2
        elif s[l-1] == ')' and s[r-1] == '(':
            pl[l-1] += 2
            pl[r-1] -= 2
        print(pl)
    else:
        if dp[l-1][r-1] + sum(pl[l-1:r]): print('No')
        else: print('Yes')