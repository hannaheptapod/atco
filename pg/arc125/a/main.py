n, m = map(int, input().split())
s = list(map(int, input().split()))
t = list(map(int, input().split()))

if any(i not in s and i in t for i in range(2)): ans = -1
else:
    shift = 0
    for i in range(1, n):
        if s[i] != s[0] or s[(-i)%n] != s[0]:
            shift = i - 1
            break
    
    ans = m
    tmp = s[0]
    flag = 0

    for ti in t:
        if ti != tmp:
            if flag == 0:
                ans += shift
                flag = 1
            ans += 1
            tmp = ti

print(ans)