"""
배열을 정렬하는 것은 쉽다. 수가 주어지면, 그 수의 각 자리수를 내림차순으로 정렬해보자.
"""

"""
def sortinside(N):
    nlist = list()
    nlist = list(map(int, nlist))
    while (int(N/10) != 0):
        nleft = N % 10
        nlist.append(nleft)
        N = int(N/10)
    nlist.append(N)

    nlist = nlist.sort()
    nreverselist = reversed(sorted(nlist))


    for i in range(len(nlist)-1):
        if(nlist[i]<nlist[i+1]):
            nlist[i],nlist[i+1] =nlist[i+1],nlist[i]

    for i in range(len(nlist)):
        print(nlist[i], end="")

"""


X = list(input())
X.sort()
X.reverse()
print(''.join(X))
