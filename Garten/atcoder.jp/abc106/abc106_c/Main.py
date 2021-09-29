s = input()
k = int(input())
slen = len(s)
for i in range(k):
    if s[i] != '1':
        ans = s[i]
        break
    else:
        ans = '1'
print(ans)