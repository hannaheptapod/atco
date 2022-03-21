N = int(input())
A = list(map(int, input().split()))
tot = [0]
for ai in A: tot.append(tot[-1]+ai)
print(A)
print(tot)
