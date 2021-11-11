n, a, b, c, d = map(int, input().split())
s = ':' + input()
if any(['##' in ss for ss in (s[a:c+1], s[b:d+1])]): ans = 'No'
elif c > d and '...' not in s[b-1:d+2]: ans = 'No'
else: ans = 'Yes'
print(ans)