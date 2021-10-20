s1 = input()
s2 = input()
s3 = input()
t = input()
ans = str()
for ti in t:
    if ti == '1': ans += s1
    elif ti == '2': ans += s2
    else: ans += s3
print(ans)