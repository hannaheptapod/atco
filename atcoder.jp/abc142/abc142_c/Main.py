n = int(input())
a = list(map(int, input().split()))
dic = {a[i-1]: i for i in range(1, n+1)}
print(*[dic[i] for i in range(1, n+1)])