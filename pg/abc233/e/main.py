I = input()
s = sum(int(a) for a in I)
X = int(I)

ans = (X*10 - s) // 9
print(ans)
