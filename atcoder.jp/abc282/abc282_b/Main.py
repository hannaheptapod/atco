def main():
    global N, M, S
    N, M = map(int, input().split())
    S = [input() for _ in range(N)]

    ans = solve()
    print(ans)


def solve():
    ret = 0
    for i in range(N-1):
        si = S[i]

        for j in range(i+1, N):
            sj = S[j]

            for k in range(M):
                if si[k] == 'x' and sj[k] == 'x': break
            else: ret += 1

    return ret


if __name__ == '__main__': main()
