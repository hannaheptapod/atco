import numpy as np

MOD = 998244353


def main():
    global N, M, K, M_inv
    N, M, K = map(int, input().split())
    M_inv = pow(M, MOD-2, MOD)
    ans = solve()
    print(ans)


def solve():
    dp = np.zeros(shape=N+1, dtype=np.int32)
    dp[-1] = 1
    for _ in range(K):
        dp[:-1] = np.convolve(
            a=np.append(arr=dp[1:], values=dp[-2:-(M+1):-1]),
            v=np.full(shape=M, fill_value=M_inv),
            mode='valid'
        ) % MOD

    return dp[0]


if __name__ == '__main__': main()
