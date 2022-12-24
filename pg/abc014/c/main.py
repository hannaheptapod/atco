def main():
    N = int(input())
    ques = [tuple(map(int, input().split())) for _ in range(N)]

    st = set()
    for a, b in ques:
        st.add(a)
        st.add(b+1)

    dic = {v: i for i, v in enumerate(sorted(st))}

    diff = [0]*(len(dic))
    for a, b in ques:
        diff[dic[a]] += 1
        diff[dic[b+1]] -= 1

    sm = 0
    ans = 0
    for d in diff:
        sm += d
        if sm > ans: ans = sm

    print(ans)


if __name__ == '__main__': main()
