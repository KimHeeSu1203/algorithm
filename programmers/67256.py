
def solution(numbers, hand):
    answer = ''

    bef_L = 10 # *을 10이라고 가정
    bef_R = 12 #*을 12라고 가정

    for i,num in enumerate(numbers):
        if num in [1,4,7]:
            answer = answer + 'L'
            bef_L = num
        elif num in [3,6,9]:
            answer = answer + 'R'
            bef_R = num
        else:
            if num == 0:
                num = 11
            L_length = abs((bef_L-1)//3-(num-1)//3) + abs((bef_L-1)%3-(num-1)%3)
            R_length = abs((bef_R-1)//3-(num-1)//3) + abs((bef_R-1)%3-(num-1)%3)
            if L_length < R_length:
                answer = answer + 'L'
                bef_L = num

            elif L_length == R_length:
                if hand == 'left':
                    answer = answer + 'L'
                    bef_L = num
                else:
                    answer = answer + 'R'
                    bef_R = num
            else:
                answer = answer + 'R'
                bef_R = num
    return answer

numbers = [1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5]
hand = "right"
print(solution(numbers,hand))


# 잘못푼 점 : 빼서 절댓값으로 하면 안됌