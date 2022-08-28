N = int(input())

e = 3.5
for _ in range(N-1): e = (int(e)*e + (int(e)+7)*(6-int(e))/2)/6

print(e)
