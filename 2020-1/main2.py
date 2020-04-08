def solution(str1, str2):
    str1 = sorted(str1)
    str2 = sorted(str2)
    if str1 == str2:
        print("순열관계이다")
    else:
        print("순열관계가 아니다")


str1 = "abcde"
str2 = "abdece"

solution(str1,str2)