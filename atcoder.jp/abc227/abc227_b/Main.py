N = int(input())
S = list(map(int, input().split()))

st = set()
for a in range(1, 1000//7 + 1):
    for b in range(1, 1000//7 + 1):
        tmp = 4*a*b + 3*a + 3*b
        if tmp > 1000: break

        st.add(tmp)

ans = sum(int(si not in st) for si in S)
print(ans)
