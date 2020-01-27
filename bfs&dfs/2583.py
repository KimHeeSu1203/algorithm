"""
첫째 줄에 M과 N, 그리고 K가 빈칸을 사이에 두고 차례로 주어진다. M, N, K는 모두 100 이하의 자연수이다.
둘째 줄부터 K개의 줄에는 한 줄에 하나씩 직사각형의 왼쪽 아래 꼭짓점의 x, y좌표값과 오른쪽 위 꼭짓점의 x, y좌표값이 빈칸을 사이에 두고 차례로 주어진다.
모눈종이의 왼쪽 아래 꼭짓점의 좌표는 (0,0)이고, 오른쪽 위 꼭짓점의 좌표는(N,M)이다. 입력되는 K개의 직사각형들이 모눈종이 전체를 채우는 경우는 없다.
"""

M,N,K = map(int,input().split()) # 가로 세로

ground = [[0 for _ in range(N)] for _ in range(M)]

for numK in range(K):
    a,b,c,d = map(int,input().split()) # 0 2 4 4
    for i in range(b,d):
        for j in range(a,c):
            ground[i][j] = 1

visit = [[False]*N for _ in range(M)]

dx = [0,0,1,-1]
dy = [-1,1,0,0]
count = 0
area = []
queue = []

for i in range(M):
    for j in range(N):
        if (ground[i][j]==0) and (not visit[i][j]):
            queue.append([i,j])
            visit[i][j] = True
            count = count + 1
            temp_area = 1
            while queue:
                _x,_y = queue.pop(0)
                for k in range(4):
                    nx = _x + dx[k]
                    ny = _y + dy[k]
                    if(0<= nx< M) and (0<= ny <N) and (not visit[nx][ny]) and (ground[nx][ny]==0):
                        queue.append([nx,ny])
                        visit[nx][ny] = True
                        temp_area = temp_area + 1
            area.append(temp_area)

area.sort()
print(count)
print(" ".join(map(str, area)))