n = int(input())
sm = 0
st = set()
for i in range(1, n+1):
    sm += i
    st.add(i)
    if sm < n: continue
    elif sm > n: st.remove(sm - n)
    break
for si in sorted(st): print(si)