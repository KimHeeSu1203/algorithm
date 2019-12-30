
N = int(input())
rope = []
for _ in range(N):
    temp_rope = int(input())
    rope.append(temp_rope)


rope.sort() # 작은 순서대로 로프
rope.reverse()

sum=[]
w = []

for i in range(N):
    sum.append(rope[i])
    temp_w = len(sum)*rope[i]
    w.append(temp_w)

print(max(w))