N,M = map(int,input().split()) # 세로가로

maze = []
for i in range(N):
    oneline = input()
    maze.append(oneline)
maze_visited = [[0 for _ in range(M)] for _ in range(N)]

all_result = [] # 이거 어디에 써야하는지 아직 모르겠음
result = 1
stack = []
stack.append([0,0])
maze_visited[0][0] = 1

while stack:
    print("stack : ",stack)
    print("result : ", result)
    [i,j] = stack.pop()
    if i == (N-1) and j == (M-1):
        maze_visited[N - 1][M - 1] = 0
        all_result.append(result)
    result += 1

    if i > 0:
        if maze[i-1][j] == '1' and maze_visited[i-1][j] == 0:
            stack.append([i-1,j])
            maze_visited[i-1][j] = 1
            #maze_visited[N-1][M-1] = 0

    if i < N-1:
        if maze[i+1][j] == '1' and maze_visited[i+1][j] == 0:
            stack.append([i+1,j])
            maze_visited[i+1][j] = 1
            #maze_visited[N - 1][M - 1] = 0

    if j > 0:
        if maze[i][j-1] == '1' and maze_visited[i][j-1] == 0:
            stack.append([i,j-1])
            maze_visited[i][j-1] = 1
            #maze_visited[N - 1][M - 1] = 0

    if j < M-1:
        if maze[i][j+1] == '1' and maze_visited[i][j+1] == 0:
            stack.append([i,j+1])
            maze_visited[i][j+1] = 1
            #maze_visited[N - 1][M - 1] = 0

print(all_result)
all_result.sort()
answer = all_result[0] - len(all_result)+1
print(answer)