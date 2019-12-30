N,M = map(int,input().split())

set = []
per = []

for _ in range(M):
    temp_set, temp_per = map(int,input().split())
    set.append(temp_set)
    per.append(temp_per)

set.sort() # 세트 가장 싼 순서
print(set)
per.sort() # 낱개 가장 싼 순서
print(per)
N_set = int(N/6) # 세트 갯수
N_per = int(N%6) # 세트 갯수

minCoin = min((N_set+1)*set[0],(N_set)*set[0]+(N_per)*per[0])
minCoin = min(minCoin,N*per[0])

print(minCoin)

