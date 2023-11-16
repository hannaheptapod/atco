def main():
    N, W = map(int, input().split())
    C = [list(map(int, input().split())) for _ in range(N)]
    C.sort(reverse=True)

    ans = solve(N, W, C)
    print(ans)


def solve(N, W, C):
    ret, sm = 0, 0

    for ai, bi in C:
        if sm + bi <= W:
            ret += ai * bi
            sm += bi
        else:
            ret += (W - sm) * ai
            break

    return ret


if __name__ == '__main__': main()
