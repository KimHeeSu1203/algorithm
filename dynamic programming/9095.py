"""
정수 4를 1, 2, 3의 합으로 나타내는 방법은 총 7가지가 있다. 합을 나타낼 때는 수를 1개 이상 사용해야 한다.

1+1+1+1
1+1+2
1+2+1
2+1+1
2+2
1+3
3+1
정수 n이 주어졌을 때, n을 1, 2, 3의 합으로 나타내는 방법의 수를 구하는 프로그램을 작성하시오.

"""


def makedynamicSum(N): #N을 구하고 싶다는 것은 size가 N+1인 상태, 즉 배열은 N이어야 함
    a = 4
    if N>3:
        while len(dp)!=(N+1):
            dp.append(dp[a-1]+dp[a-2]+dp[a-3])
            a = a+1
    print(dp[N])



dp=[]
dp.append(0)
dp.append(1)
dp.append(2)
dp.append(4)
N = int(input())
makedynamicSum(N)
