p = list(map(int, input().split()))
alpha = 'abcdefghijklmnopqrstuvwxyz'
s = str()
for i in range(26): s = s + alpha[p[i]-1]
print(s)