a, b, k = map(int, input().split())
s = set([i for i in range(a, a+k)] + [j for j in range(b, b-k, -1)])
l = sorted(s)
_ = [print(li) for li in l if li >= a and li <= b]