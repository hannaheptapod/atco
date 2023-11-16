def main():
    h1, h2, h3, w1, w2, w3 = map(int, input().split())

    ans = solve(h1, h2, h3, w1, w2, w3)
    print(ans)


def solve(h1, h2, h3, w1, w2, w3):
    from itertools import product

    cnt = 0
    for a, b, d, e in product(range(1, 30), repeat=4):
        c = h1 - a - b
        f = h2 - d - e
        g = w1 - a - d
        h = w2 - b - e
        i = w3 - c - f

        if c > 0 and f > 0 and g > 0 and h > 0 and i > 0 and (g + h + i) == h3: cnt += 1

    return cnt


if __name__ == '__main__': main()
