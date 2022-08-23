from itertools import product, combinations

H_1, W_1 = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(H_1)]
H_2, W_2 = map(int, input().split())
B = [list(map(int, input().split())) for _ in range(H_2)]

for bit_y, bit_x in product(combinations(range(H_1), H_2), combinations(range(W_1), W_2)):

    for i, j in product(range(H_2), range(W_2)):
        if A[bit_y[i]][bit_x[j]] != B[i][j]: break

    else:
        ans = 'Yes'
        break

else: ans = 'No'

print(ans)
