n = int(input())
a = list(map(int, input().split()))
ans = a.index(sorted(a, reverse=True)[1]) + 1
print(ans)