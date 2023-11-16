def main():
    global N, H
    N = int(input())
    H = list(map(int, input().split()))

    ans = solve()
    print(ans)


def solve():
    res, mx = 0, 0
    for i, h in enumerate(H):
        if h >= mx: res, mx = i+1, h

    return res


if __name__ == '__main__': main()
