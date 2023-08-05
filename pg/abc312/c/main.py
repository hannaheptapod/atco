from bisect import bisect_left, bisect_right

def main():
    N, M = map(int, input().split())
    A = sorted(list(map(int, input().split())))
    B = sorted(list(map(int, input().split())))

    def check(mid):
        seller = bisect_right(A, mid)
        buyer = M - bisect_left(B, mid)

        return seller >= buyer

    ng, ok = -1, 10**9+1
    while abs(ok - ng) > 1:
        mid = (ok + ng) // 2
        if check(mid): ok = mid
        else: ng = mid
    
    print(ok)

if __name__ == "__main__": main()
