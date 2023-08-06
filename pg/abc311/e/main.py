def main():
    H, W, N = map(int,input().split())
    set_hole = set(tuple(map(lambda x: int(x)-1, input().split())) for _ in range(N))

    
    def solve():
        dp = [[0]*W for _ in range(H)]

        ans = 0
        for i in range(H):
            for j in range(W):
                if (i, j) in set_hole: continue
                dp[i][j] = min([dp[i-1][j-1], dp[i][j-1], dp[i-1][j]]) + 1
                ans += dp[i][j]

        return ans
    

    ans = solve()
    print(ans)

    return


if __name__ == '__main__': main()
