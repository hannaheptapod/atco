S = input()

for si in S:
    cnt = sum(int(si == sj) for sj in S)

    if cnt == 1:
        print(si)
        break
else: print(-1)
