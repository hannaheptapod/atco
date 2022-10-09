from bisect import bisect


def main():
    N, _ = map(int, input().split())
    H = sorted(map(int, input().split()))
    W = sorted(map(int, input().split()))

    E, O = [0], [0]
    for i in range(N-1):
        if not i%2: E.append(E[-1] + H[i+1] - H[i])
        else: O.append(O[-1] + H[i+1] - H[i])

    ans = float('inf')
    for w in W:
        idx = bisect(H, w)
        if idx%2: ids -= 1

    print(ans)


if __name__ == '__main__': main()
