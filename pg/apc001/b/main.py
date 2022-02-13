n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

diff = sum(b)-sum(a)
sm_a = sm_b = 0

for ai, bi in zip(a, b):
    if ai < bi:
        sm_a += -((ai-bi)//2)
        sm_b += (ai-bi)%2
    elif ai > bi: sm_b += ai-bi

if diff>=sm_a and sm_a>=sm_b: ans = 'Yes'
else: ans = 'No'

print(ans)