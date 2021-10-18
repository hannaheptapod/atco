s = input()
size = len(s)
ans = -1
for l in range(size):
    for r in range(1, size+1):
        slr = s[l:r]
        leng = len(slr)
        if leng%2 or leng == size: continue
        else:
            if slr[:leng//2] == slr[leng//2:]: ans = max(ans, leng)
print(ans)