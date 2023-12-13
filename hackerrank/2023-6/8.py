# KinderGarten Adventures


def main():
    n = int(input())
    t = list(map(int, input().split()))
    ans = solve(n, t)
    print(ans)


def solve(n, t):
    diff = [0] * n

    for i, ti in enumerate(t):
        if ti == 0:
            diff[0] += 1
        else:
            diff[(i + 1) % n] += 1
            diff[(i + 1 + ti) % n] -= 1

    acm = [0] * (n + 1)
    mx, idx = 0, 0
    for i in range(n):
        acm[i + 1] = acm[i] + diff[i]
        if acm[i + 1] > mx:
            mx, idx = acm[i + 1], i + 1

    return idx


if __name__ == '__main__': main()
