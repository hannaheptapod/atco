def main():
    N, X, Y, Z = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    S = [[i+1, ai, bi, ai+bi] for i, (ai, bi) in enumerate(zip(A, B))]

    ans = set()

    cnt = 0
    for (i, ai, bi, si) in sorted(S, key=lambda x: x[1], reverse=True):
        if cnt >= X: break
        if i in ans: continue
        ans.add(i)
        cnt += 1
    for (i, ai, bi, si) in sorted(S, key=lambda x: x[2], reverse=True):
        if cnt >= X+Y: break
        if i in ans: continue
        ans.add(i)
        cnt += 1
    for (i, ai, bi, si) in sorted(S, key=lambda x: x[3], reverse=True):
        if cnt >= X+Y+Z: break
        if i in ans: continue
        ans.add(i)
        cnt += 1

    ans = sorted(ans)
    _ = [print(i) for i in ans]


if __name__ == '__main__': main()
