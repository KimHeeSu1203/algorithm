"""

정수 X에 사용할 수 있는 연산은 다음과 같이 세 가지 이다.

X가 3으로 나누어 떨어지면, 3으로 나눈다.
X가 2로 나누어 떨어지면, 2로 나눈다.
1을 뺀다.
정수 N이 주어졌을 때, 위와 같은 연산 세 개를 적절히 사용해서 1을 만들려고 한다. 연산을 사용하는 횟수의 최솟값을 출력하시오..

"""

def make1(X):
    time = 0
    while X != 1:
        time += 1
        if X%3==0:
            X = X / 3
            print(X)
        elif X%2 == 0:
            X = X/2
            print(X)
        else:
            X = X-1
            print(X)
    print(time)
    return time

X = int(input())

make1(X)