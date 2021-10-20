a, b = map(int, input().split())
s = input()
num = '0123456789'
for i in range(a + b + 1):
    if (i == a and s[i] != '-') or (i != a and s[i] not in num):
        ans = 'No'
        break
    else: continue
else: ans = 'Yes'
print(ans)