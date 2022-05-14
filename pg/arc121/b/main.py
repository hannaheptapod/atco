import bisect

N = int(input())
dic = {c: [] for c in 'RGB'}
for _ in range(2*N):
    a, c = input().split()
    bisect.insort(dic[c], int(a))


def diff(x, y):
    res = 10**15
    i, j = 0, 0
    while i < len(dic[x]) and j < len(dic[y]):
        res = min(res, abs(dic[x][i] - dic[y][j]))

        if dic[x][i] < dic[y][j]: i += 1
        elif dic[x][i] > dic[y][j]: j += 1
        else: i, j = i+1, j+1

    return res


if not any([len(dic[x])%2 for x in 'RGB']): ans = 0
elif len(dic['R'])%2 and len(dic['G'])%2: ans = min(diff('R', 'G'), diff('G', 'B')+diff('B', 'R'))
elif len(dic['G'])%2 and len(dic['B'])%2: ans = min(diff('G', 'B'), diff('B', 'R')+diff('R', 'G'))
else: ans = min(diff('B', 'R'), diff('R', 'G')+diff('G', 'B'))

print(ans)
