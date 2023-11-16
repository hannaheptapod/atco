def main():
    N, M = map(int, input().split())
    prods = [list(map(int, input().split())) for _ in range(N)]
    for i in range(N): prods[i] = [prods[i][0], set(prods[i][2:])]

    prods.sort(key=lambda x: -x[0])
    for i in range(N):
        pi, si = prods[i]
        for j in range(i+1, N):
            pj, sj = prods[j]

            if sj >= si and (pi > pj or sj > si): break
        else: continue
        ans = 'Yes'
        break
    else: ans = 'No'

    print(ans)


if __name__ == '__main__': main()
