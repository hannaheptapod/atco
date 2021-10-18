n, m = map(int, input().split())
a = [[0, 2*n-i, input()] for i in range(2*n)]

for i in range(m):
    for k in range(n):
        l, r = a[2*k][2][i], a[2*k+1][2][i]
        if (l == 'G' and r == 'C') or (l == 'C' and r == 'P') or (l == 'P' and r == 'G'): a[2*k][0] += 1
        elif (l == 'G' and r == 'P') or (l == 'C' and r == 'G') or (l == 'P' and r == 'C'): a[2*k+1][0] += 1
    a.sort(reverse=True)

_ = [print(2*n - a[i][1] + 1) for i in range(2*n)]