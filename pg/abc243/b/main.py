N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

p, q = 0, 0
for i in range(N):
    if A[i] == B[i]: p += 1
    elif A[i] in B: q += 1

print(p)
print(q)
