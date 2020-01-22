def BFS(N,M,box):
    time = 0

    queue = []
    visit = [[0 for _ in range(N)] for _ in range(M)]
    print(visit)

    for i in range(M):
        for j in range(N):
            if box[i][j] == '1' and visit[i][j] == 0:
                queue.append([i, j])
                visit[i][j] = 1

            while queue:
                time += 1
                tmp = []
                [a,b] = queue.pop(0)

                if a > 0 :
                    if visit[a-1][b] == 0 and box[a - 1][b] == '0':
                        box[a - 1][b] = '1'
                        queue.append([a - 1, b])
                if b > 0 :
                    if visit[a][b-1] == 0 and box[a][b - 1] == '0':
                        box[a][b - 1] = '1'
                        queue.append([a, b - 1])
                if a < M - 1 :
                    if visit[a+1][b] == 0 and box[a + 1][b] == '0':
                        box[a + 1][b] = '1'
                        queue.append([a + 1, b])
                if b < N - 1 :
                    if visit[a][b+1] == 0 and box[a][b + 1] == '0':
                        box[a][b + 1] = '1'
                        queue.append([a, b + 1])

                #if tmp:
                #    print(tmp)
                #    time += 1
                #queue.extend(tmp)

                for i in range(M):
                    print(box[i])
                print()
    print("time:", time)
    return box



N,M = map(int,input().split())

box = []
result = []
for i in range(M):
    one_line = input().split()
    box.append(one_line)

result = BFS(N,M,box)

for i in range(M):
    if '0' in result[i]:
        print("-1")
