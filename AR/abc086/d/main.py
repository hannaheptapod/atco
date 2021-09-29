n, k = map(int, input().split())
def intorstr(src):
    if src == 'B' or src == 'W':
        return src
    else:
        return int(src)
xyc = [list(map(intorstr, input().split())) for _ in range(n)]
