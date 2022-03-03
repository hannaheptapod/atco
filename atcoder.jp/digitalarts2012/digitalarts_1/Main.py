list_s = list(input().split())
N = int(input())
list_t = [input() for _ in range(N)]

def filtering(s):
    leng = len(s)
    
    for t in list_t:
        if leng != len(t): continue
        
        for j in range(leng):
            if s[j] != t[j] and t[j] != '*': break
        else: return '*'*leng

    return s

ans = []
for s in list_s: ans.append(filtering(s))

print(*ans)
