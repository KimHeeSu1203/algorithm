def solution(bridge_length, weight, truck_weights):
    answer = 0
    bridge = [0 for _ in range(bridge_length)]
    while(truck_weights):
        answer += 1
        if((sum(bridge[1:])+truck_weights[0]) > weight): # 무게 더나가면
            bridge.append(0)
            bridge.pop(0)
        else:
            bridge.append(truck_weights[0])
            truck_weights.pop(0)
            bridge.pop(0)
    answer += bridge_length
    return answer


bridge_length = 2
weight = 10
truck_weights = [7,4,5,6]
print(solution(bridge_length, weight, truck_weights))