s = input()
a, b, c, d = map(int, list(si for si in s))
pm = ('+', '-')
for i in range(2):
    for j in range(2):
        for k in range(2):
            if a + b*(-1)**i + c*(-1)**j + d*(-1)**k == 7: ans = str(a)+pm[i]+str(b)+pm[j]+str(c)+pm[k]+str(d)+'=7'
print(ans)