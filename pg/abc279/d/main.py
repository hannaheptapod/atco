def main():
    global A, B
    A, B = map(int, input().split())

    idx = binary_search()
    ans = min([B*x + A/pow(x+1, 0.5) for x in (idx, idx+1)]) if idx >= 0 else A
    print(ans)


def binary_search():
    ok, ng = -1, 10**18

    def is_ok(x): return B - A*pow(x+1, -1.5)/2 < 0
    while abs(ok - ng) > 1:
        md = (ok + ng)//2
        if is_ok(md): ok = md
        else: ng = md

    return ok


if __name__ == '__main__': main()
