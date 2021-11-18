n = int(input())
s = input()
mod = 10**9 + 7
dic = {}
for si in s:
    if si not in dic: dic[si] = 1
    dic[si] += 1
ans = 1
for di in dic:
    ans = ans * dic[di] % mod
ans -= 1
print(ans)