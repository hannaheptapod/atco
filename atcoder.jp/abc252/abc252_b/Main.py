N, K = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

mx = max(A)
for bi in B:
    if A[bi-1] == mx:
        ans = 'Yes'
        break
else: ans = 'No'
print(ans)
