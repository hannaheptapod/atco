def main():
    global N, S, Q, queries
    N = int(input())
    S = input()
    Q = int(input())
    queries = [input().split() for _ in range(Q)]

    ans = solve()
    print(ans)

    return


def solve():
    status = [[0, si] for si in S]
    fill = None

    for i, (t, x, c) in enumerate(queries):
        if t == '1': status[int(x)-1] = [i, c]
        else: fill = [i, t]

    res_list = [si[1] for si in status]
    for i, (t, c) in enumerate(status):
        if not fill or t >= fill[0]: continue
        if fill[1] == '2': res_list[i] = c.lower()
        else: res_list[i] = c.upper()

    return ''.join(res_list)


if __name__ == '__main__': main()
