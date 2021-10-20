N = int(input())
S = input()
tmp = sum(s=='E' for s in S[1:N])
ans = tmp
for i in range(1, N):
    tmp = tmp + (S[i-1]=='W') - (S[i]=='E')
    if tmp < ans:
        ans = tmp
    if ans == 0:
        break
    else:
        continue
print(ans)