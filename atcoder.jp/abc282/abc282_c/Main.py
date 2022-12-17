def main():
    N = int(input())
    S = input()

    ans = solve(N, S)
    print(ans)


def solve(N, S):
    arr = ['']*N

    is_closed = False
    for i, si in enumerate(S):
        if si == '"': is_closed = not is_closed
        if si == ',' and not is_closed: si = '.'

        arr[i] = si

    return ''.join(arr)


if __name__ == '__main__': main()
