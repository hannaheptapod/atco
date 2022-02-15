n, k = map(int, input().split())

ans = (n//k)**3 + (k%2 == 0)*((n+k//2)//k)**3

print(ans)