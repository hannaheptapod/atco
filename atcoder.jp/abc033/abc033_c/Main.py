S = input()

mems = list(S.split('+'))
ans = sum([int('0' not in mi) for mi in mems])
print(ans)
