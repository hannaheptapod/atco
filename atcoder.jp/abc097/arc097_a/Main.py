from bisect import bisect, insort

s = input()
K = int(input())

arr = []
for l in range(len(s)):
    for r in range(l+1, len(s)+1):
        slr = s[l:r]

        if slr in arr: continue
        if bisect(arr, slr) < K: insort(arr, slr)
        else: break

ans = arr[K-1]
print(ans)
