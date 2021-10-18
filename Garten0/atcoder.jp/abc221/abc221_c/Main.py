from itertools import permutations

n = input()
arr = [n[i] for i in range(len(n))]
mx = str(max([int(ai) for ai in arr]))
arr.remove(mx)
lst = list(permutations(arr))
len = len(n)
ans = -1
for li in lst:
    l = [mx] + list(li)
    for i in range(1, -(-len//2) + 1):
        sl, tl = l[:i], l[i:]
        s, t = ''.join(sli for sli in sl), ''.join(tli for tli in tl)
        if t[0] == '0': continue
        else:
            tmp = int(s) * int(t)
            if tmp > ans: ans = tmp
print(ans)