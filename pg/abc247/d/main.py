from collections import deque

Q = int(input())

ans = []
deq = deque()
for _ in range(Q):
    c = list(map(int, input().split()))

    if not deq: deq.append((c[1], c[2]))

    elif c[0] == 1:
        l = deq.pop()
        if l[0] == c[1]: deq.append((l[0], l[1] + c[2]))
        else:
            deq.append(l)
            deq.append((c[1], c[2]))

    else:
        sm, cnt = 0, 0
        while cnt < c[1]:
            l = deq.popleft()
            if cnt + l[1] <= c[1]: sm += l[0]*l[1]
            else:
                sm += l[0]*(c[1] - cnt)
                deq.appendleft((l[0], cnt + l[1] - c[1]))

            cnt += l[1]
        ans.append(sm)

print(*ans, sep='\n')
