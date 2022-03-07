S = input()
K = int(input())

leng = len(S)
sm = [0]
for si in S: sm.append(sm[-1]+int(si == 'X'))

ok, ng = 0, leng+1
while ok+1 < ng:
    md = (ok + ng)//2
    
    for l in range(leng-md + 1):
        if sm[l+md]-sm[l]+K >= md:
            ok = md
            break
    else: ng = md

ans = ok
print(ans)
