def solution(participant, completion):

    for i in completion:
        participant.remove(i)

    print(participant)
    answer = ''.join(participant)
    return answer

participant = ["leo", "kiki", "eden"]
completion = ["eden", "kiki"]

print(solution(participant,completion))