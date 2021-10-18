n = int(input())
cap = [int(input()) for _ in range(5)]
ans = 4 + -(-n//min(cap))
print(ans)