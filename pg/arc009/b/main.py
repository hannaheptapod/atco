b = list(input().split())
N = int(input())

d_cvt = {b[i]:str(i) for i in range(10)}
d_rec = {str(i):b[i] for i in range(10)}
def cvt(x, reverse):
    y = ''

    if not reverse:
        for xi in x: y += d_cvt[xi]
    else:
        for xi in x: y += d_rec[xi]

    return y

a = [int(cvt(input(), 0)) for _ in range(N)]
a.sort()

_ = [print(cvt(str(ai), 1)) for ai in a]