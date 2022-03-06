N = int(input())
s = [input()[::-1] for _ in range(N)]
s.sort()

print(*[si[::-1] for si in s], sep='\n')
