s = input()
leng = len(s)
ans = 753
for i in range(leng - 2):
    ans = min(ans, abs(753 - int(s[i:i+3])))
print(ans)