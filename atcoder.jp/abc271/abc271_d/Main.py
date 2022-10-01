def main():
    N, S = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    res = solve(N, S, arr)
    if res:
        print('Yes')
        print(res)
    else:
        print('No')


def solve(N, S, arr):
    cards = [[h > t, abs(h-t)] for h, t in arr]
    mn = sum(arr[i][cards[i][0]] for i in range(N))
    mx = sum(arr[i][1-cards[i][0]] for i in range(N))

    if mn > S: return False

    turns = [turn for turn, _ in cards]
    if mn == S: return make(turns)

    dp = [[False]*(10100+1) for _ in range(N+1)]
    dp[0][0] = True

    for i in range(N):
        for j in range(mx-mn+1):
            if dp[i][j]:
                dp[i+1][j] = True
                if j+cards[i][1] <= mx-mn: dp[i+1][j+cards[i][1]] = True

    if not dp[N][S-mn]: return False

    sm = S
    for i in range(N-1, -1, -1):
        if not sm: break
        if not dp[i][sm-mn]:
            turns[i] = 1-cards[i][0]
            sm -= cards[i][1]

    return make(turns)


def make(turns): return ''.join('T' if turn else 'H' for turn in turns)


if __name__ == '__main__': main()
