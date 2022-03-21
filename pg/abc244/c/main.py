N = int(input())

nums = set(i for i in range(1, 2*N + 2))
for _ in range(N):
    x = nums.pop()
    print(x)
    y = int(input())
    nums.remove(y)

print(nums.pop())
y = int(input())

print('', flush=True)
