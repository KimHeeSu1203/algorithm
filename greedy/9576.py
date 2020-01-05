"""
학생들 요구에 모든 책 다 있으면 책 수만큼 나눠줄 수 있고
만약에 없으면 그 수만큼 뺴면 된다.
학생은 하나로 묶여있기 떄문에 한 책 받으면 pop 해서 없애버려야 한다.
"""
def sortK(item,k):
    return item[k]

caseTest = int(input())
for i in range(caseTest):
    student_list = []
    N,M = map(int, input().split()) # 엔은 책 수, 엠은 학생 수
    book_flag = [0 for _ in range(N+1)] # 0은 안볼 것

    #book_list = 0
    #student_flag = [0 for _ in range(M)]
    for j in range(M):
        temp_list = list(map(int,input().split()))
        range_a = sortK(temp_list,0)
        range_b = sortK(temp_list,1)+1
        temp_temp_list = list(map(lambda x: x, range(range_a,range_b)))
        student_list.append(temp_temp_list)
    print(student_list)



    """
    for j in range(1,N+1): # 찾을 책 넘버
        print(j)
        for k in range(M):
            if (j in student_list[k]) & (student_flag[k] == 0):
                book_list =  book_list + 1
                student_flag[k] = 1

    print(student_flag)
    print(book_list)
"""

"""
1
2 3
1 2
1 2
1 2
"""