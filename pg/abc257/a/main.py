N, X = map(int, input().split())

ans = chr(ord('A')+(X-1)//N)
print(ans)
