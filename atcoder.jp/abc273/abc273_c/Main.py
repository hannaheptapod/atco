def main():
    N = int(input())
    A = list(map(int, input().split()))
    st = sorted(set(A))
    dic = {st[i]: len(st)-i-1 for i in range(len(st))}

    ans = [0]*N
    for ai in A: ans[dic[ai]] += 1

    print(*ans, sep='\n')


if __name__ == '__main__': main()
