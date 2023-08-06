from collections import deque


def main():
    N, M = map(int,input().split())
    S = [input() for _ in range(N)]

    
    def dfs():
        seen = [[0]*M for _ in range(N)]
        deq = deque([(1, 1)])

        cnt = 1
        while deq:
            i, j = deq.popleft()
            if seen[i][j] == 2: continue
            seen[i][j] = 2

            for di, dj in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                ni, nj = i+di, j+dj
            
                while S[ni][nj] == '.':
                    if seen[ni][nj] == 0:
                        cnt += 1
                        seen[ni][nj] = 1
                    
                    ni, nj = ni+di, nj+dj
                
                if seen[ni-di][nj-dj] < 2: deq.append((ni-di, nj-dj))
            
        return cnt


    ans = dfs()
    print(ans)

    return


if __name__ == '__main__': main()
