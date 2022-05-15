N = int(input())

st = set()
ans, mx = 0, 0
for i in range(N):
    s, t = input().split()
    t = int(t)

    if s not in st and t > mx: ans, mx = i+1, t
    st.add(s)

print(ans)
