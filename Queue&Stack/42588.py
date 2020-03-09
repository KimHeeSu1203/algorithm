def solution(heights):
    answer = [0 for _ in range(len(heights))]
    print(answer)
    for num in range(len(heights)-1,-1,-1):
        x = heights[num]
        for i in range(num-1,-1,-1):
            print("i",i)
            if(heights[i] > x):
                answer[num] = i+1
                break
    return answer


heights = [6,9,5,7,4]
print(solution(heights))