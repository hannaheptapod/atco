def main():
    global N, S, T
    N = int(input())
    S, T = input(), input()

    sm_s, sm_t = sum(int(si) for si in S), sum(int(ti) for ti in T)
    if (sm_s - sm_t)%2: ans = -1
    elif sm_s == sm_t: ans = '0'*N
    elif sm_s > sm_t:
        arr = ['0']*N
        cnt = (sm_s - sm_t)//2
        for i in range(N-1, -1, -1):
            if S[i] == '1' and T[i] == '0':
                arr[i] = '1'
                cnt -= 1
            if cnt == 0: break
        ans = ''.join(arr)
    else:
        arr = ['0']*N
        cnt = (sm_t - sm_s)//2
        for i in range(N-1, -1, -1):
            if S[i] == '0' and T[i] == '1':
                arr[i] = '1'
                cnt -= 1
            if cnt == 0: break
        ans = ''.join(arr)

    print(ans)


if __name__ == '__main__': main()
