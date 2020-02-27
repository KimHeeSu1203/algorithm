def solution(phone_book):
    answer = True
    phone_book.sort()
    for i in range(len(phone_book)-1):
        size = len(phone_book[i])
        if phone_book[i] == phone_book[i+1][0:size]:
            answer = False
            break
    return answer

phone_book = ["119", "97674223", "1195524421"]
print(solution(phone_book))

