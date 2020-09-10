# 앞부터 차례대로 잘라나가서 뒤에 있나확인하는 함수 하나

"""
def makeZip(s):
    for size in range(1,len(s)//2+1):
        answer = ""
        bef_R = 0
        aft_R = size

        while aft_R < len(s)-1:
            sZip = s[bef_R:aft_R]
            count = 1

            while sZip == s[aft_R:aft_R+size]:
                count = count + 1
                print("szip",sZip,"bef_R",bef_R,"aft_R",aft_R)
                print(count)
                bef_R = aft_R
                aft_R = aft_R + size
                answer = answer+str(count) + sZip

            else:
                bef_R = aft_R
                aft_R = aft_R + size
                answer = answer + sZip


        print(answer)

def makeZip(s):
    for size in range(1, len(s) // 2 + 1):
        answer = ""
        bef_R = 0
        aft_R = size

        while aft_R < len(s) - 1:
            sZip = s[bef_R:aft_R]
            count = 1

            bef_R = aft_R
            aft_R = aft_R + size

            if(sZip == s[aft_R:aft_R + size]):
                count = count + 1
                print("szip", sZip, "bef_R", bef_R, "aft_R", aft_R)
                print(count)
                bef_R = aft_R
                aft_R = aft_R + size
                answer = answer + str(count) + sZip

            else:
                answer = answer + sZip

        print(answer)
"""
# 최종 길이랑 현재랑 비교해서 어떤게 나은지 확인하는 함수 하나



def makeZip(s):
    minAnswer = len(s)
    for size in range(1, len(s)//2 + 1):
        temp = []
        answer = ""
        for j in range(0,len(s),size):
            temp.append(s[j:j+size])
        sZip = temp[0]
        zipCount = 1
        for words in temp[1:]:
            if sZip == words:
                zipCount = zipCount+1
            else:
                if(zipCount != 1):
                    answer = answer + str(zipCount) + sZip

                else:
                    answer = answer + sZip

                sZip = words
                zipCount=1

        if (zipCount != 1):
            answer = answer + str(zipCount) + sZip
        else:
            answer = answer + sZip

        if len(answer) < minAnswer:
            minAnswer = len(answer)
    return minAnswer
# 결과 내보내는 함수 하나
print(makeZip("aaabcaaabc"))