
def solution(phone_book):
    answer = True
    phone_book.sort(key=lambda x: (len(x), x))

    for k in range(len(phone_book)-1):
        if phone_book[k] in phone_book[k+1]:
            answer = False

    return answer

#phone_book = ["119", "97674223", "1195524421"]
phone_book = ["123", "789", "456"]
print(solution(phone_book))
