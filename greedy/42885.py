def solution(people, limit):
    answer = 0
    visit = [0 for _ in range(len(people))]
    print(visit)
    people.sort()
    for i in range(len(people)):
        if(visit[i] == 0):
            min = people[i]
            visit[i] = 1
            for j in range(len(people)-1,i,-1):
                if(min+people[j] <= limit) and (visit[j] ==0): #합이 낮고, 들린 적 없으면
                    visit[j] = 1
            answer += 1
    return answer


people = [20, 70, 80, 50]
limit = 100

print(solution(people,limit))


##배 2척 말고 3척, 4척이 넘게도 합쳐 질 수 있다는 점을