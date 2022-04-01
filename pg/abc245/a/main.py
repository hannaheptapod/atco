A, B, C, D = map(int, input().split())

tak, aok = 60*A + B, 60*C + D + 0.1

ans = 'Takahashi' if tak < aok else 'Aoki'
print(ans)
