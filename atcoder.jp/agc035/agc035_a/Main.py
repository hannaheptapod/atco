n = int(input())
a = list(map(int, input().split()))

x = [[], []]
for ai in a:
    if ai not in x[0]:
        x[0] += [ai]
        x[1] += [0]

    x[1][x[0].index(ai)] += 1
    
    if len(x[0]) <= 3: continue
    ans = 'No'
    break
else:
    if len(x[0]) == 1 and x[0][0] == 0: ans = 'Yes'
    elif len(x[0]) == 2 and 0 in x[0] and 3*x[1][x[0].index(0)] == n: ans = 'Yes'
    elif len(x[0]) == 3 and x[0][0]^x[0][1]^x[0][2] == 0 and all([3*x1 == n for x1 in x[1]]): ans = 'Yes'
    else: ans = 'No'

print(ans)