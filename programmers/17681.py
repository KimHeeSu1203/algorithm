def makeBinary(n,arr):
    binaryArr = []
    for i in range(len(arr)):
        binaryN = []
        num = arr[i]
        for _ in range(n):
            binaryN.append(num%2)
            num = num // 2
        binaryN.reverse()
        binaryArr.append(binaryN)
    return binaryArr

def solution(n, arr1, arr2):
    binary1 = makeBinary(n,arr1)
    binary2 = makeBinary(n,arr2)
    binary = [["#" for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if (binary1[i][j]+binary2[i][j])==0:
                binary[i][j] = " "
        binary[i] = "".join(binary[i])
    return binary

def solution2(n, arr1, arr2):
    answer = []
    for i,j in zip(arr1, arr2):
        print(i,j)
        a12 = str(bin(i|j))
        print(a12)

n = 6
arr1 = [46, 33, 33 ,22, 31, 50]
arr2 = [27 ,56, 19, 14, 14, 10]
#print(solution(n,arr1, arr2))

solution2(n,arr1,arr2)
