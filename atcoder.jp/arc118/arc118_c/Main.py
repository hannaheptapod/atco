N = int(input())

A = [i for i in range(1, 10**4 + 1) if not all([i%j for j in (6, 10, 15)])]
print(*(A[:N] if N > 3 else [6, 10, 15]))
