def main():
    global H, W, ans
    H, W, A, B = map(int, input().split())

    ans = 0
    dfs(0, 0, A, B)
    print(ans)


def dfs(i, bit, a, b):
    if i == H*W:
        global ans
        ans += 1
        return

    if bit>>i & 1:
        dfs(i+1, bit, a, b)
        return

    if b: dfs(i+1, bit | 1<<i, a, b-1)
    if a:
        if i%W < W-1 and not bit>>(i+1) & 1: dfs(i+1, bit | 1<<i | 1<<(i+1), a-1, b)
        if i+W < H*W: dfs(i+1, bit | 1<<i | 1<<(i+W), a-1, b)


if __name__ == '__main__': main()
