N = int(input())

MOD = N%26

if MOD in (8, 10): ans = 1
elif MOD in (16, 18, 20): ans = 2
elif MOD in (24, 2, 4): ans = 3
elif MOD in (6, 12, 14): ans = 4
elif MOD == 22: ans = 5
else: ans = 0

print(ans)