def main():
    N, M = map(int, input().split())

    rep, d, e = 1, 0, 0
    for i in range(1, N+1):
        for j in range(9, 0, -1):
            if not rep*j % M:
                d, e = j, i
                break
        rep = (10*rep + 1) % M

    ans = ''.join([str(d)]*e) if d else '-1'
    print(ans)


if __name__ == '__main__': main()
