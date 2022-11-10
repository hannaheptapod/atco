from collections import Counter


def main():
    H, W, M = map(int, input().split())
    st = set()
    row, col = Counter(), Counter()
    for _ in range(M):
        h, w = map(int, input().split())
        st.add((h, w))
        row[h] += 1
        col[w] += 1

    row, col = (c.most_common()+[(0, 0)] for c in (row, col))
    print(row, col)

    ans = row[0][1] + col[0][1]
    if row[0][0] > row[0][1] and col[0][0] > col[0][1] and (row[0][0], col[0][0]) in st: ans -= 1

    print(ans)


if __name__ == '__main__': main()
