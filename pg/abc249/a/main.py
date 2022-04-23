A, B, C, D, E, F, X = map(int, input().split())

tak = B * (A*(X // (A + C)) + min(X%(A + C), A))
aok = E * (D*(X // (D + F)) + min(X%(D + F), D))

if tak > aok: ans = 'Takahashi'
elif tak < aok: ans = 'Aoki'
else: ans = 'Draw'

print(ans)
