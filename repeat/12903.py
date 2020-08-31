def solution(s):
    answer = ''
    lenS = len(s)
    if lenS%2 == 0:
        answer = s[lenS//2-1:lenS//2+1]
    else:
        answer = s[lenS//2]
    return answer


def solution2(s):
    return s[(len(s)-1)//2:len(s)//2+1]


s1 = "abcde"
s2 = "qwered"

print(solution2(s1))

