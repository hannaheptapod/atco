S = input()
T = input()

ans = 'Yes' if len(S) <= len(T) and S == T[:len(S)] else 'No'
print(ans)
