N = int(input())

nbr = {j: [] for j in (1, 2)}

mx = 0
for i in range(3, N+1):
    for j in range(1, 2+1):
        q = ['?', j, i]
        print(*q)
        d = int(input())
        if d == 1: nbr[j].append(i)
        mx = max(mx, d)

ll = len(nbr[1])*len(nbr[2])
if not ll: ans = 1
elif len(nbr[1]) == 1:
    if ll == 1:
        q = ['?', nbr[1], nbr[2]]
        print(*q)
        d = int(input())
        ans = d+2 if d < mx else d-2
    else:
        st = set()
        for j in nbr[2][:min(4, len(nbr[2]))]:
            q = ['?', nbr[1], j]
            print(*q)
            d = int(input())
            st.add(d)
        ans = min(st) if len(st) == 1 else min(st)+2
elif len(nbr[2]) == 1:
    st = set()
    for j in nbr[1][:min(4, len(nbr[1]))]:
        q = ['?', nbr[2], j]
        print(*q)
        d = int(input())
        st.add(d)
