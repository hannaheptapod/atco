from math import gcd
N, A, B = map(int, input().split())


def lcm(x, y): return x*y // gcd(x, y)


ans = N*(N+1)//2 - A*(N//A)*(N//A+1)//2 - B*(N//B)*(N//B+1)//2 + \
    lcm(A, B)*(N//lcm(A, B))*(N//lcm(A, B)+1)//2
print(ans)
