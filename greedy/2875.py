N,M,K = map(int,input().split())

if (N/2) >= M:
    max = M

else:
    max = N//2

left = M+N - (max*3)
while (K > left):
    max = max - 1
    left = M + N - (max * 3)


print(max)


"""
team = 0
left = M+N - (team*3)

while((team<=M) & (M*2<=N) & (left>=K)):
    team = team+1
    left = M+N - (team*3)
    print(left)

print(team)
"""




"""
all = N + M
team = M
while N < 2*M:
    team = team-1

left = M+N - (3*team)

while left <= K:
    team = team - 1
    left = all - (3*team)

print(team)
"""