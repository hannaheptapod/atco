n = int(input())
for i in range(10):
    if 2**i <= n: ans = 2**i
    else: break
print(ans)