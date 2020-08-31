def solution(answers):
    stu = [[1, 2, 3, 4, 5],[2, 1, 2, 3, 2, 4, 2, 5],[3, 3, 1, 1, 2, 2, 4, 4, 5, 5]]
    answer_list = [0 for _ in range(3)]
    answer = []

    for i in range(len(stu)): # 학생수만큼
       for j in range(len(answers)):#문제만큼
           if answers[j] == stu[i][j%len(stu[i])]:
               answer_list[i] = answer_list[i]+1
    maxCorrect = max(answer_list)

    for i,k in enumerate(answer_list):
        if k == maxCorrect:
            answer.append(i+1)

    return answer


answers = [1,3,2,4,2]
print(solution(answers))