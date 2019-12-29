money_type = []
type, sum = map(int,input().split())

for _ in range(type):
    money_type.append(int(input()))

money_type.reverse()
coin = 0
for i in range(type):
    if money_type[i]>sum:
        continue
    else:
        coin = coin + int(sum/money_type[i])
        sum = sum%money_type[i]

print(coin)