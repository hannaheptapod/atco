K = int(input())

s = bin(K)[2:]
ans = ''
for si in s: ans += str(2*int(si))

print(ans)
