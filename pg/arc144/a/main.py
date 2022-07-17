N = int(input())

M = 2*N
x = '4'*(N//4)
x = str(N%4)+x if N%4 else x

print(M)
print(x)
