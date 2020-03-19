from collections import defaultdict

def solution(tickets):
    answer = []
    plane = defaultdict(list)
    for x in tickets:
        key, value = x[0], x[1]
        plane[key].append(value)
        plane[key].sort()
    start = "ICN"
    while plane[start]:
        answer.append(start)
        next = plane[start].pop(0)
        start = next
    answer.append(start)
    return answer

tickets = [["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL", "SFO"]]
print(solution(tickets))