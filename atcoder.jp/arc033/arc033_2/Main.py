N_A, N_B = map(int, input().split())
A = set(input().split())
B = set(input().split())

ans = len(A & B)/len(A | B)

print(ans)