N = int(input())
a = sorted(zip(range(1, N+1), map(int, input().split())), key=lambda x: x[1], reverse=True)

_ = [print(ai[0]) for ai in a]
