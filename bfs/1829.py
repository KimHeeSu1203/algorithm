#[카카오 프렌즈 컬러링북]
"""
6 4
1 1 1 0
1 2 2 0
1 0 0 1
0 0 0 1
0 0 0 3
0 0 0 3
"""
M,N = map(int, input().split()) #M이 세로 N이 가로
oneLine = []
ground = []
for _ in range(M):
    oneLine = input().split()
    ground.append(oneLine)

visit = [[False]*N for _ in range(M)]
all_queue = []
queue = []
dx = [0,0,1,-1]
dy = [-1,1,0,0]
"""
for i in range(M):
    for j in range(N):
        if ground[i][j] is not '0':
            print("-----")
            print(ground[i][j])
            print(i,j,"0아니다")

        else:
            print("-----")
            print(ground[i][j])
            print(i,j,"0이다")
"""
for i in range(M):
    for j in range(N):
        if (not visit[i][j]) and (ground[i][j] is not '0'):
            queue.append([i,j])
            one_block = []
            one_block.append([i,j])
            visit[i][j] = True
            while queue:
                _x, _y = queue.pop(0)
                origin = ground[_x][_y]
                for k in range(4):
                    nx = _x + dx[k]
                    ny = _y + dy[k]
                    if(0<=nx<M) and (0<=ny<N) and (not visit[nx][ny]) and (ground[nx][ny] == origin):
                        queue.append([nx,ny])
                        one_block.append([nx,ny])
                        visit[nx][ny] = True
            all_queue.append(one_block)

all_size = []
for i in range(len(all_queue)):
    size = len(all_queue[i])
    all_size.append(size)
all_size.sort()

print(len(all_queue),all_size[-1])