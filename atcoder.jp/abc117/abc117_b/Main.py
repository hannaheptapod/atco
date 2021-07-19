n = int(input())
l = list(map(int, input().split()))
l.sort()
if sum(l) / l[n - 1] > 2:
    print('Yes')
else:
    print('No')