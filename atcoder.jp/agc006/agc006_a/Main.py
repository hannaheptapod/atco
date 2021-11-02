n = int(input())
s, t = input(), input()
for i in range(n):
    if s[:i] + t[:n-i] != s: continue
    print(n + i)
    break
else: print(2 * n)