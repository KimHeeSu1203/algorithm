from collections import deque

def solution(bridge_length, weight, truck_weights):
    answer = 0
    bridge = deque(0 for _ in range(bridge_length))
    truck_weights = deque(truck_weights)
    
    while(truck_weights):
        answer += 1
        if((sum(list(bridge)[1:])+truck_weights[0]) > weight): # 무게 더나가면
            bridge.append(0)
            bridge.popleft()
        else:
            bridge.append(truck_weights[0])
            truck_weights.popleft()
            bridge.popleft()
    answer += bridge_length
    return answer


bridge_length = 2
weight = 10
truck_weights = [7,4,5,6]
print(solution(bridge_length, weight, truck_weights))