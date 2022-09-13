from itertools import product


def main():
    global N, F, P
    N = int(input())
    F = [list(map(int, input().split())) for _ in range(N)]
    P = [list(map(int, input().split())) for _ in range(N)]

    ans = calc()
    print(ans)


def calc():
    ret = -10**15
    for bits in product([0, 1], repeat=10):
        if not any(bits): continue
        tmp = 0

        for i in range(N):
            cnt = 0
            for j in range(10):
                if bits[j] and F[i][j]: cnt += 1
            tmp += P[i][cnt]

        ret = max(ret, tmp)
    return ret


if __name__ == '__main__': main()
