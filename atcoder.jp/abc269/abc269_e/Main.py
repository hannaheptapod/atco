def main():
    global N
    N = int(input())
    u, b, l, r = 0, N, 0, N

    while abs(u-b) > 1: u, b = query('i', u, b)
    while abs(l-r) > 1: l, r = query('j', l, r)

    print('!', b, r, flush=True)


def query(s, mn, mx):
    md = -(-(mn+mx)//2)
    if s == 'i':
        print('?', mn+1, md, 1, N, flush=True)
        ans = int(input())

        if ans == md-mn: return md, mx
        else: return mn, md

    elif s == 'j':
        print('?', 1, N, mn+1, md, flush=True)
        ans = int(input())

        if ans == md-mn: return md, mx
        else: return mn, md


if __name__ == '__main__': main()
