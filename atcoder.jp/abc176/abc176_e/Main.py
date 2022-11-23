from collections import Counter


def main():
    H, W, M = map(int, input().split())
    st = set()
    rows, cols = Counter(), Counter()
    for _ in range(M):
        h, w = map(int, input().split())
        st.add((h, w))
        rows[h] += 1
        cols[w] += 1

    rows, cols = (cnt.most_common()+[(0, 0)] for cnt in (rows, cols))

    ans = rows[0][1] + cols[0][1]
    rows, cols = ([i for i, n in arr if n == arr[0][1]] for arr in (rows, cols))

    for r in rows:
        for c in cols:
            if (r, c) not in st: break
        else: continue
        break
    else: ans -= 1

    print(ans)


if __name__ == '__main__': main()
