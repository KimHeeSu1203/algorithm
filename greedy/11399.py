time = []

N = int(input())
time = list(map(int,input().split()))
time.sort()
sum = 0
tmp_sum = 0

for i in range(N):
    tmp_sum = tmp_sum + time[i]
    sum = sum + tmp_sum
print(sum)
