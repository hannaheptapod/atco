n = int(input())

ans = min(min(abs(x-i) + n - x*i for i in range(1, n//x + 1)) for x in range(1, n+1))
print(ans)
