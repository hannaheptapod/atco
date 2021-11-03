n = int(input())
a = list(map(int, input().split()))
nl = [0]*3
for ai in a:
    if ai%2: nl[0] += 1
    elif ai%4: nl[1] += 1
    else: nl[2] += 1
if nl[0]-int(nl[1] == 0) <= nl[2]: ans = 'Yes'
else: ans = 'No'
print(ans)