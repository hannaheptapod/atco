S = input()

ans = 0
for i in range(10**4):
    p = format(i, '04')
    for j in range(10):
        if (S[j] == 'o' and str(j) not in p) or (S[j] == 'x' and str(j) in p): break
    else: ans += 1

print(ans)