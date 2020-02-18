def solution(people, limit):
    answer = 0
    people.sort()

    min = 0
    max = len(people)-1

    while(min <= max):
        #print("max, min, answer", max,people[max], min,people[min], answer)
        if(people[min] + people[max] <= limit):
            answer += 1
            min += 1
            max -= 1
        else:
            answer += 1
            max -= 1

    return answer


people = [80, 80, 80, 80, 20]
limit = 100

print(solution(people,limit))
