def main():
    N = int(input())
    S = [input() for _ in range(N)]

    st, s_s, s_n = set(), set(), set()
    for s in S: st.add(s), s_s.add(s[0]), s_n.add(s[1])

    suits = {'S', 'H', 'C', 'D'}
    nums = {'A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K'}
    ans = 'Yes' if len(st) == N and s_s <= suits and s_n <= nums else 'No'
    print(ans)


if __name__ == '__main__': main()
