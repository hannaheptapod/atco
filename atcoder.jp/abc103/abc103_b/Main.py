s, t = input()*2, input()
for i in range(len(t)):
    if s[i:len(t)+i] == t:
        ans = 'Yes'
        break
else: ans = 'No'
print(ans)