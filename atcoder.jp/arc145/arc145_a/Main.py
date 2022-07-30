N = int(input())
S = input()

ans = 'Yes' if S[0] == S[-1] or N >= 3 and (S[0] == 'B' or S[-1] == 'A') else 'No'
print(ans)
