from bisect import bisect


def main():
    N = int(input())
    P = list(map(int, input().split()))

    l = 0
    for i in range(N-1, 0, -1):
        if P[i-1] > P[i]:
            l = i
            break

    tail = sorted(P[l:])
    idx_h = bisect(tail, P[l-1])-1
    head = tail[idx_h]
    tail[idx_h] = P[l-1]
    tail.reverse()

    ans = P[:l-1] + [head] + tail
    print(*ans)


if __name__ == '__main__': main()
