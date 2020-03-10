def solution(priorities, location):
    answer_list = []
    num_priorities = []
    for i in range(len(priorities)):
        tmp_all = [i,priorities[i]]
        num_priorities.append(tmp_all)
    answer_num = num_priorities[location]

    while(priorities):
        priorities.sort(reverse=True)
        max_num = priorities[0]
        pri_y = num_priorities[0][1]
        if pri_y < max_num:
            num_priorities.append(num_priorities.pop(0))

        else:
            answer_list.append(num_priorities.pop(0))
            priorities.pop(0)
    return answer_list.index(answer_num)+1

priorities =[1, 1, 9, 1, 1, 1]
location = 0
print(solution(priorities, location))