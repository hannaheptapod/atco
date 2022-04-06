A, B = map(int, input().split())


def f(y): return y//4 - y//100 + y//400


ans = f(B) - f(A-1)
print(ans)
