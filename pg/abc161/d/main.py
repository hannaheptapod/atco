k = int(input())

n = i = 0

while i < k:
    n += 1
    s = str(n)

    if all([abs(int(s[j+1])-int(s[j]))<=1 for j in range(len(s)-1)]): i += 1

ans = n

print(ans)