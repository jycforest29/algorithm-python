import sys
from collections import deque
input = sys.stdin.readline

r, c = map(int, input().split())
board = [list(input().rstrip()) for _ in range(r)]
visit = [[0 for _ in range(c)] for _ in range(r)]
dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]

r_idx, c_idx = 0, 0
for i in range(r):
    for j in range(c):
        if board[i][j] == 'S':
            r_idx, c_idx = i, j

q = deque([[r_idx, c_idx, 0]])
visit[r_idx][c_idx] = 1
ans = 0
while q:
    popped = q.popleft()

    if board[popped[0]][popped[1]] == 'D':
        ans = popped[2]
        break

    for i in range(r):
        for j in range(c):
            if board[i][j] == '*':
                for k in range(4):
                    wr = i+dr[k]
                    wc = j+dc[k]

                    if 0 <= wr < r and 0 <= wc < c and not visit[wr][wc]:
                        if board[wr][wc] == '.':
                            board[wr][wc] = '*'
            
    for i in range(4):
        tr = popped[0]+dr[i]
        tc = popped[1]+dc[i]

        if 0 <= tr < r and 0 <= tc < c and not visit[tr][tc]:
            if (board[tr][tc] == '.' or board[tr][tc] == 'D'):
                visit[tr][tc] = 1
                q.append([tr, tc, popped[2]+1])

if ans:
    print(ans)
else:
    print("KAKTUS")
