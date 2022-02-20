a, b, c = map(int, input().split())

if (a+b)==2*c or (b+c)==2*a or (c+a)==2*b: ans = 'Yes'
else: ans = 'No'

print(ans)