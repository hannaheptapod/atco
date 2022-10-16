from collections import defaultdict
import array
from bisect import insort, bisect


def main():
    global y, x, arr_v, arr_h
    H, W, y, x = map(int, input().split())
    arr_v = defaultdict(lambda: array.array('i', [0, H+1]))
    arr_h = defaultdict(lambda: array.array('i', [0, W+1]))
    N = int(input())
    for _ in range(N):
        r, c = map(int, input().split())
        insort(arr_v[c], r)
        insort(arr_h[r], c)

    Q = int(input())
    for _ in range(Q):
        d, l = input().split()
        y, x = move(d, int(l))
        print(y, x)


def move(d, l):
    ret_y, ret_x = y, x
    if d == 'L': ret_x = max(x-l, arr_h[y][bisect(arr_h[y], x)-1] + 1)
    elif d == 'R': ret_x = min(x+l, arr_h[y][bisect(arr_h[y], x)] - 1)
    elif d == 'U': ret_y = max(y-l, arr_v[x][bisect(arr_v[x], y)-1] + 1)
    elif d == 'D': ret_y = min(y+l, arr_v[x][bisect(arr_v[x], y)] - 1)
    return ret_y, ret_x


if __name__ == '__main__': main()
