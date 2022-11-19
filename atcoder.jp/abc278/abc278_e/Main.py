from collections import defaultdict


def main():
    H, W, N, h, w = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(H)]

    dic = defaultdict(lambda: [H, 0, W, 0])
    for i, row in enumerate(A):
        for j, a in enumerate(row):
            dic[a] = [
                min(dic[a][0], i), max(dic[a][1], i),
                min(dic[a][2], j), max(dic[a][3], j)
            ]

    C = len(dic)
    for i in range(H-h+1):
        ansi = [C]*(W-w+1)

        for j in range(W-w+1):
            for y_min, y_max, x_min, x_max in dic.values():
                if i > y_min or i+h-1 < y_max: continue
                if j > x_min or j+w-1 < x_max: continue
                ansi[j] -= 1

        print(*ansi)


if __name__ == '__main__': main()
