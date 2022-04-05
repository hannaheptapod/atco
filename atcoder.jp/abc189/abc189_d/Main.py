N = int(input())
S = [input() == 'OR' for _ in range(N)]

good = 1
for i in range(N): good += 2**(i+1) if S[i] else 0

print(good)
