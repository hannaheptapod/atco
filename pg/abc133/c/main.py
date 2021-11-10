l, r = map(int, input().split())
mod = 2019
if l//mod == r//mod: ans = min([min([i*j % mod for j in range(i+1, r%mod+1)]) for i in range(l%mod, r%mod)])
else: ans = 0
print(ans)