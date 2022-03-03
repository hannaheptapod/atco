S = list(map(int, input().split()))
G = list(map(int, input().split()))

if S == G: ans = 0
elif any((sum(S) == sum(G),
          S[0]-S[1] == G[0]-G[1],
          abs(S[0]-G[0]) + abs(S[1]-G[1]) <= 3)): ans = 1
elif any((sum(S)%2 == sum(G)%2,
          abs(sum(S) - sum(G)) <= 3,
          abs((S[0]-S[1]) - (G[0]-G[1])) <= 3,
          abs(S[0]-G[0]) + abs(S[1]-G[1]) <= 6)): ans = 2
else: ans = 3

print(ans)
