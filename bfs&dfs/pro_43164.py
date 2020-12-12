answer = []
def dfs(route, left_ticket):
    if len(left_ticket) == 0 :
        answer.append(route)
        return

    for ticket in left_ticket:
        if route[-1] == ticket[0]:
            tmp_go = route.copy()
            tmp_left = left_ticket.copy()
            # 지금 갈 곳은 ticket, ticket[1]이 도착지
            tmp_go.append(ticket[1])
            tmp_left.pop(tmp_left.index(ticket))
            dfs(tmp_go,tmp_left)


def solution(tickets):
    start = ["ICN"]
    dfs(start,tickets)
    answer.sort(key = lambda x: (len(x),x))
    return answer[0]



tickets = [["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]
solution(tickets)