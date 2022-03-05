N, M = map(int, input().split())

ans = pow(10, N, mod=M**2)//M % M
print(ans)
