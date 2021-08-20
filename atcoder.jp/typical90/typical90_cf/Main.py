def nc2(n):
    if n == 1: return 0
    else: return n * (n - 1) // 2

n = int(input())
s = input()

ans = nc2(n)
n_tmp = 1
s_tmp = s[0]
for i in range(1, n):
    if s[i] == s_tmp: n_tmp += 1
    else:
        ans -= nc2(n_tmp)
        n_tmp = 1
        s_tmp = s[i]
    if i == n - 1: ans -= nc2(n_tmp)
print(ans)