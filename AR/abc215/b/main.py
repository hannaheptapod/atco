#import

n = int(input())
# = map(int, input().split())
# = list(map(int, input().split()))
# = [list(map(int, input().split())) for _ in range()]

k = 0
while n > 1:
    n >>= 1
    k += 1
print(k)