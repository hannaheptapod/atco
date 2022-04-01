A, B, C = map(int, input().split())

ans = 'Takahashi' if (C == 0 and A > B) or (C == 1 and A >= B) else 'Aoki'
print(ans)
