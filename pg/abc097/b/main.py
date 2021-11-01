n = int(input())
eset = {1}
for i in range(2, int(n**0.5) + 1):
    ei = i**2
    while ei <= n:
        eset.add(ei)
        ei *= i
elist = list(eset)
elist.sort()
for ei in elist:
    if ei <= n: ans = ei
    else: break
print(ans)