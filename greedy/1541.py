
all = input().split("-")

for i in range(len(all)):
    if ('+' in all[i]):
        all[i] = sum(int(x) for x in all[i].split('+'))
sum = int(all[0])
for i in range(1,len(all)):
    sum = sum - int(all[i])
print(sum)

"""

#import sys
#import re

# +,- 기준으로 split하고 delimiter도 없애지 않는다
#equation = re.split("(\\+|-)", sys.stdin.readline().strip())
#print(equation)


all = all.replace("-0","-")
all = all.replace("+0","+")



makeAll = []
flag = 0
for i in range(len(all)):
    if (all[i] == '-') & (flag == 0):
        makeAll.append(all[i])
        makeAll.append('(')
        flag = 1

    elif (all[i] == '-') & (flag == 1):
        makeAll.append(')')
        makeAll.append(all[i])
        makeAll.append('(')

    elif (all[i] == '+'):
        makeAll.append(all[i])

    elif (i == len(all)-1) & (flag == 1):
        makeAll.append(all[i])
        makeAll.append(')')
        flag = 0
    else:
        makeAll.append(all[i])


print(makeAll)
join_All = ""
for i in range(len(makeAll)):
    join_All += makeAll[i]

print("aaaaaaa")
print(join_All)
join_All.replace("^0+","")
print(join_All.
#result = exec(join_All)
#print(result)



"""
"""
n = [sum(int(x) for x in y.split('+')) for y in input().split('-')]
print(n)
print(sum)
print(n[0] - sum(n[1:]))

"""

