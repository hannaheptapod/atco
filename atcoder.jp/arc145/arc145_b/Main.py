N, A, B = map(int, input().split())

if A <= B: ans = max(0, N-A+1)
else: ans = B*((N-A+1)//A) + min((N-A+1)%A, B) if N >= A else 0
print(ans)
