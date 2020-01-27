

def bfs(I,now_x,now_y):
    dx = [2, 1, -1, -2, -2, -1, 1, 2]
    dy = [1, 2, 2, 1, -1, -2, -2, -1]

    visit = [[False]*I for _ in range(I)]
    count = [[0]*I for _ in range(I)]
    queue = []
    queue.append([now_x,now_y])
    visit[now_x][now_y] = True

    while queue:
        _x,_y = queue.pop(0)
        if (_x == next_x) and (_y == next_y):
            return count[_x][_y]
        else:
            for k in range(8):
                nx = _x + dx[k]
                ny = _y + dy[k]
                if(0<=nx<I) and (0<=ny<I) and not visit[nx][ny] :
                    queue.append([nx,ny])
                    visit[nx][ny] = True
                    count[nx][ny] = count[_x][_y] + 1
    return -1

test_time = int(input())
for _ in range(test_time):
    I = int(input())
    now_x, now_y = map(int,input().split())
    next_x,next_y = map(int,input().split())
    print(bfs(I,now_x,now_y))

"""
test_time = int(input())
result = []
for _ in range(test_time):
    I = int(input())
    now_x, now_y = map(int,input().split())
    next_x,next_y = map(int,input().split())
    result.append(bfs(I,now_x,now_y))

for k in range(len(result)):
    print(result[k])
"""