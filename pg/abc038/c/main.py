N = int(input())
a = list(map(int, input().split()))

def isIncreased():
    if l == r: return True
    elif a[r-1] < a[r]: return True

    return False

ans = 0
l, r = 0, 0
while l < N and r < N:
    if isIncreased():
        ans += r-l + 1
        r += 1
    else: l = r

print(ans)
