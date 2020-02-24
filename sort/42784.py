def solution(array, commands):
    answer = []
    for l in range(len(commands)):
        i, j, k = commands[l][0],commands[l][1],commands[l][2]
        new_array = array[i-1:j]
        new_array.sort()
        print("new_array", new_array)
        tmp_answer = new_array[k-1]
        answer.append(tmp_answer)
    return answer

array = [1, 5, 2, 6, 3, 7, 4]
commands = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]
print(solution(array, commands))