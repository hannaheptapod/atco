def main():
    global N, M, A
    N, M = map(int, input().split())
    A = list(map(int, input().split()))

    st = make_set()

    ans = [mex(sorted(s)) for s in st[1:]]
    print(*ans, sep='\n')


def make_set():
    st = [set() for _ in range(M+1)]

    for i in range(N):
        ai = A[i]

        fr = max(0, -int(ai//(i+1)))
        ai += fr*(i+1)

        for x in range(fr, M+1):
            if ai > N: break
            st[x].add(ai)
            ai += i+1

    return st


def mex(arr):
    ng, ok = -1, len(arr)

    while abs(ok-ng) > 1:
        md = (ok+ng)//2
        if arr[md] > md: ok = md
        else: ng = md

    return ok


if __name__ == '__main__': main()
