A, B, K = map(int, input().split())

route = [[1]*(B+1) for _ in range(A+1)]
for i in range(1, A+1):
    for j in range(1, B+1):
        route[i][j] = route[i-1][j] + route[i][j-1]


def find_kth(i, j, k):
    if i == 0: return 'b'*j

    if j == 0: return 'a'*i

    if k <= route[i-1][j]: return 'a' + find_kth(i-1, j, k)

    return 'b' + find_kth(i, j-1, k - route[i-1][j])


ans = find_kth(A, B, K)
print(ans)
