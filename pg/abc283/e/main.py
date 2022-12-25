from itertools import product


def main():
    H, W = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(H)]

    dp = [[[H]*2 for _ in range(2)] for _ in range(H)]
    dp[0][0][0], dp[0][0][1] = 0, 1

    for i, j, k, l in product(range(1, H), range(2), range(2), range(2)):
        x, y, z = A[i-2] if i != 1 else [-1]*W, A[i-1], A[i]
        if j: x = [1-xi for xi in x]
        if k: y = [1-yi for yi in y]
        if l: z = [1-zi for zi in z]

        is_ok = True
        for m in range(W):
            not_ver = x[m] != y[m] and y[m] != z[m]
            not_hor = (m == 0 or y[m] != y[m-1]) and (m == W-1 or y[m] != y[m+1])
            if not_ver and not_hor: is_ok = False

        if i == H-1:
            for m in range(W):
                not_ver = z[m] != y[m]
                not_hor = (m == 0 or z[m] != z[m-1]) and (m == W-1 or z[m] != z[m+1])
                if not_ver and not_hor: is_ok = False

        if is_ok: dp[i][k][l] = min(dp[i][k][l], dp[i-1][j][k]+l)

    ans = H
    for j, k in product(range(2), range(2)): ans = min(ans, dp[H-1][j][k])
    if ans == H: ans = -1
    print(ans)


if __name__ == '__main__': main()
