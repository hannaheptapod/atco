n = int(input())
t = input()
s = '110' * (10**5)
a = b = c = 0
if s[:n] == t: a += 1
if s[1:n + 1] == t: b += 1
if s[2:n + 2] == t: c += 1
m = -(-n // 3)
ans = (a + b + c) * (10**10 - m)
if n % 3 == 0: ans += a
elif n % 3 == 1: ans += a + b + c
else: ans += a + b
print(ans)