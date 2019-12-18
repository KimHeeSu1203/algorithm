"""
수 N개 A1, A2, ..., AN이 주어진다. A를 오름차순 정렬했을 때, 앞에서부터 K번째 있는 수를 구하는 프로그램을 작성하시오.
"""

size, k = input().split()
size = int(size)
k = int(k)
N = []*size
N = input().split()
N = list(map(int,N))
N.sort()
print(N[k-1])
