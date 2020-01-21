"""
<그림 1>과 같이 정사각형 모양의 지도가 있다. 1은 집이 있는 곳을, 0은 집이 없는 곳을 나타낸다.
철수는 이 지도를 가지고 연결된 집들의 모임인 단지를 정의하고, 단지에 번호를 붙이려 한다. 여기서 연결되었다는 것은 어떤 집이 좌우,
혹은 아래위로 다른 집이 있는 경우를 말한다. 대각선상에 집이 있는 경우는 연결된 것이 아니다. <그림 2>는 <그림 1>을 단지별로 번호를 붙인 것이다.
도를 입력하여 단지수를 출력하고, 각 단지에 속하는 집의 수를 오름차순으로 정렬하여 출력하는 프로그램을 작성하시오.
"""
N = int(input())

apart = []
for i in range(N):
    one_line = input()
    apart.append(one_line)

visit_apart = [[0 for _ in range(N)] for _ in range(N)]
queue = []
all_result = []

for i in range(N):
    for j in range(N):
        result = 0
        if (visit_apart[i][j] == 0) & (apart[i][j] == '1'): # 아직 안들렸고 아파트 있으면
            visit_apart[i][j] = 1
            queue.append([i,j])
            result +=1

            while queue:
                [a, b] = queue.pop(0)
                if (a > 0):
                    if(visit_apart[a - 1][b] == 0 and apart[a - 1][b] == '1'):
                        visit_apart[a - 1][b] = 1
                        queue.append([a - 1, b])
                        result += 1

                if (a + 1 < N):
                    if (visit_apart[a + 1][b] == 0 and apart[a + 1][b] == '1'):
                        visit_apart[a + 1][b] = 1
                        queue.append([a + 1, b])
                        result += 1

                if (b > 0):
                    if(visit_apart[a][b-1] == 0 and apart[a][b - 1] == '1'):
                        visit_apart[a][b - 1] = 1
                        queue.append([a, b - 1])
                        result += 1

                if (b + 1 < N):
                    if (visit_apart[a][b+1] == 0 and apart[a][b + 1] == '1'):
                        visit_apart[a][b + 1] = 1
                        queue.append([a, b + 1])
                        result += 1
            all_result.append(result)

print(len(all_result))
all_result.sort()
for i in range(len(all_result)):
    print(all_result[i])


