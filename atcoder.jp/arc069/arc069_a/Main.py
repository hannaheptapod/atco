n, m = map(int, input().split())
print(min(m//2, n + (m - 2*n)//4))