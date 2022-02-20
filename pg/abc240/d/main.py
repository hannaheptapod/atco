N = int(input())
a = list(map(int, input().split()))
l = []

ans = 0

for ai in a:
    ans += 1

    if len(l) == 0: l.append([ai, 1])
    elif l[-1][0] != ai: l.append([ai, 1])
    elif l[-1][1]+1 < ai: l[-1][1] += 1
    else:
        l = l[:-1]
        ans -= ai
    
    print(ans)