N, K, X = map(int, input().split())
A = list(map(int, input().split()))

if sum([ai//X for ai in A]) > K: ans = sum(A) - K*X
elif sum([-int(-ai//X) for ai in A]) <= K: ans = 0
else:
    mod = {}
    for ai in A:
        if ai%X not in mod: mod[ai%X] = 0
        mod[ai%X] += 1

    mod = sorted(mod.items(), reverse=True)

    ans = sum([x*y for x, y in mod])
    coup = K - sum([ai//X for ai in A])

    for x, y in mod:
        if coup <= 0: break

        use = min(coup, y)
        ans -= x*use
        coup -= use

print(ans)
