n = int(input())
s = input()
x = 0
ans = 0
for si in s:
    x += int(si == 'I') - int(si == 'D')
    ans = max(x, ans)
print(ans)