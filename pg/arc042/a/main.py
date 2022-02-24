N, M = map(int, input().split())
a = reversed(list(int(input()) for _ in range(M)))

ans = []
st = set()
for ai in a:
    if ai not in st:
        st.add(ai)
        ans.append(ai)
for i in range(1, N + 1):
    if i not in st: ans.append(i)

print(*ans, sep='\n')