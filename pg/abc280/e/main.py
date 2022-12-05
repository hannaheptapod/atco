MOD = 998244353
H_inv = pow(100, MOD-2, MOD)


def main():
    N, P = map(int, input().split())

    ans = calc_ev(N, P)
    print(ans)


def calc_ev(N, P):
    if P == 0: return N
    if P == 100: return -(-N//2)

    dp = [0]*(N+2)

    for i in range(N):
        dp[i+1] += (dp[i]+1)*(100-P)*H_inv
        dp[i+1] %= MOD

        dp[i+2] += (dp[i]+1)*P*H_inv
        dp[i+2] %= MOD

    return (dp[N-1]+1)%MOD


if __name__ == '__main__': main()
