K = int(input())

st, now, cnt = set(), 7, 1
while True:
    if now%K == 0:
        ans = cnt
        break
    elif now%K in st:
        ans = -1
        break

    st.add(now%K)
    now = (10*now + 7)%K
    cnt += 1

print(ans)
