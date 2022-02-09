N = int(input())

for h in range(N//4 + 1, 3*N//4 + 1):
    for n in range(N*h//(4*h - N) + 1, 2*N*h//(4*h - N) + 1):
        if N*h*n%(4*h*n - N*(h + n)): continue
        w = N*h*n // (4*h*n - N*(h + n))
        break
    else: continue
    break

print(h, n, w)