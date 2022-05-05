A = input()
N = len(A)
cnt = sum([A[i] != A[N-i-1] for i in range(N)])

if cnt >= 4: ans = 25*N
elif cnt == 2: ans = 25*N - 2
elif N%2: ans = 25*(N-1)
else: ans = 25*N

print(ans)
