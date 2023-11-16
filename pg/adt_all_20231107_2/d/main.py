def main():
    R, C = map(int, input().split())
    B = [input() for _ in range(R)]

    ans = solve(R, C, B)
    print(ans)


def solve(R, C, B):
    after = [[B[i][j] for j in range(C)] for i in range(R)]

    for i in range(R):
        for j in range(C):
            if B[i][j] in ('.', '#'): continue

            power = int(B[i][j])
            for k in range(R):
                for l in range(C):
                    if abs(i-k) + abs(j-l) <= power: after[k][l] = '.'

    return '\n'.join(''.join(after[i]) for i in range(R))


if __name__ == '__main__': main()
