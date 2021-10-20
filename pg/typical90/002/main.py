n = int(input())

def cvt(l):
    dst = str()
    for li in l:
        if li == '0':
            dst += '('
        else:
            dst += ')'
    return dst

if n % 2 == 1:
    print()

else:
    for i in range(2**n):
        bi_str = format(i, '0'+str(n)+'b')
        num = [0] * 2
        flag = 0
        for bi in bi_str:
            num[int(bi)] += 1
            if num[0] < num[1] or num[0] > n//2:
                flag = 1
                break
            else:
                continue
        if flag == 0:
            print(cvt(bi_str))