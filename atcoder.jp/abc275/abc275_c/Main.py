def main():
    S = [input() for _ in range(9)]

    ans = solve(S)
    print(ans)


def solve(S):
    ret = 0

    for i in range(8):
        for j in range(8):
            for k in range(1, 9-max(i, j)):
                for l in range(k):
                    p = ((i+l, j), (i+k, j+l), (i+k-l, j+k), (i, j+k-l))
                    if all(S[x][y] == '#' for x, y in p): ret += 1

    return ret


if __name__ == '__main__': main()
