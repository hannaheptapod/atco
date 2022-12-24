def main():
    H, W = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(H)]

    dp = [[[H]*2 for _ in range(2)] for _ in range(H)]
    dp[0][0][0] = 0
    dp[0][0][1] = 1

    for i in range(1, H):
        for j in range(2):
            for k in range(2):
                for l in range(2):
                    x = [-1]*W
                    if i != 1: x = A[i-2]
                    if j: x = [1-xi for xi in x]
                    y = A[i-1]
                    if k: y = [1-yi for yi in y]
                    z = A[i]
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
    for j in range(2):
        for k in range(2):
            ans = min(ans, dp[H-1][j][k])
    if ans == H: ans = -1
    print(ans)


if __name__ == '__main__': main()
