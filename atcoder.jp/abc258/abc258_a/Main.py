K = int(input())

if K < 60: ans = '21:'+f'{K:02}'
else: ans = '22:'+f'{K-60:02}'
print(ans)
