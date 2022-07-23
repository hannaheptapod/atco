N, C = map(int, input().split())
op = [list(map(int, input().split())) for _ in range(N)]


def bit(x, i): return x>>i & 1


ans = [0]*N
for k in range(30):
    func = [0, 1]
    crr = bit(C, k)

    for i in range(N):
        f = [-1, -1]
        x = bit(op[i][1], k)

        if op[i][0] == 1: f = [0&x, 1&x]
        elif op[i][0] == 2: f = [0|x, 1|x]
        else: f = [0^x, 1^x]

        func = [f[func[0]], f[func[1]]]
        crr = func[crr]
        ans[i] |= crr << k

print(*ans, sep='\n')
