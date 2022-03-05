from itertools import product

N = int(input())
X = list(map(int, input().split()))

P = [p for p in range(2, max(X)+1) if all([p%q for q in range(2, int(p**0.5)+1)])]
num_p = len(P)
b_x = [''.join(str(int(x%p == 0)) for p in P) for x in X]

ans = P[-1]**num_p
for bi in map(lambda x: ''.join(x), product('01', repeat=num_p)):
    if all([int(bi, 2)&int(bx_j, 2) for bx_j in b_x]):
        tmp = 1

        for j in range(num_p):
            if int(bi, 2) & 1<<(num_p-j-1): tmp *= P[j]
        
        ans = min(ans, tmp)
        
print(ans)
