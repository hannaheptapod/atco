def main():
    A, B, C, D, E, F = map(int, input().split())
    wat, sug = set(), set()

    for i in range(31):
        if 100*A*i > F: break

        for j in range(31):
            if 100*A*i + 100*B*j > F: continue
            wat.add(100*A*i + 100*B*j)

    for i in range(3001):
        if C*i > F: break

        for j in range(3001):
            if C*i + D*j > F: continue
            sug.add(C*i + D*j)

    wat, sug = sorted(wat), sorted(sug)

    ans = [0, -1]
    for w in wat:
        if w > F: break

        for s in sug:
            if 100*s > E*w or w + s > F: continue
            if s*ans[0] > (w + s)*ans[1]: ans = [w + s, s]

    print(*ans)


if __name__ == '__main__': main()
