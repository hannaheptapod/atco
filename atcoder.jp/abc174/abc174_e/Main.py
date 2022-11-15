def main():
    global N, K, A
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort(reverse=True)

    ans = binary_search()
    print(ans)


def binary_search():
    ng, ok = 0, A[0]

    def is_ok(x):
        sm = 0

        for ai in A:
            if ai < x: return sm <= K
            sm += -(-ai//x) - 1

        return sm <= K

    while abs(ok - ng) > 1:
        md = (ng + ok)//2
        if is_ok(md): ok = md
        else: ng = md

    return ok


if __name__ == '__main__': main()
