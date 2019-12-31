all = input()
makeAll = []
flag = 0 # flag가 1이라는 것은 ( 여기서 마무리했다는 것
for i in range(len(all)):
    print(all[i])
    if (all[i] == '-') & (flag == 0): # 마이너스 뒷부분만 젤 크게 만들어주면 되는것?
        print("11111111")
        makeAll.append(all[i])
        makeAll.append('(')
        flag = 1

    elif (all[i] == '-') & (flag == 1): # 마이너스 뒷부분만 젤 크게 만들어주면 되는것? -(    -
        print("2222222")
        makeAll.append(')')
        makeAll.append(all[i])
        makeAll.append('(')

    elif (all[i] == '+'):
        print("33333333")
        makeAll.append(all[i])

    elif (i == len(all)-1) & (flag == 1):
        print("444444444")
        makeAll.append(all[i])
        makeAll.append(')')
        flag = 0

    else:
        print("555555555")
        makeAll.append(all[i])
    print("flag", flag)
    print("-------------")



join_All = ""
for i in range(len(makeAll)):
    join_All += makeAll[i]
print(join_All)
result = eval(join_All)
print(result)