N,M = map(int,input().split()) # 세로가로

maze = []
for i in range(N):
    oneline = input()
    maze.append(oneline)
maze_visited = [[0 for _ in range(M)] for _ in range(N)]
maze_count = [[0 for _ in range(M)] for _ in range(N)]
queue = []
queue.append([0, 0])
maze_visited[0][0] = 1
maze_count[0][0] = 1

while queue:
    [i,j] = queue.pop(0)
    if i == (N-1) and j == (M-1):
        result = maze_count[N-1][M-1]
        print(result)

    if i > 0:
        if maze[i-1][j] == '1' and maze_visited[i-1][j] == 0:
            queue.append([i-1,j])
            maze_visited[i-1][j] = 1
            maze_count[i-1][j] = maze_count[i][j] + 1

    if i < N-1:
        if maze[i+1][j] == '1' and maze_visited[i+1][j] == 0:
            queue.append([i+1,j])
            maze_visited[i+1][j] = 1
            maze_count[i+1][j] = maze_count[i][j] + 1

    if j > 0:
        if maze[i][j-1] == '1' and maze_visited[i][j-1] == 0:
            queue.append([i,j-1])
            maze_visited[i][j-1] = 1
            maze_count[i][j-1] = maze_count[i][j] + 1

    if j < M-1:
        if maze[i][j+1] == '1' and maze_visited[i][j+1] == 0:
            queue.append([i,j+1])
            maze_visited[i][j+1] = 1
            maze_count[i][j+1] = maze_count[i][j] + 1
