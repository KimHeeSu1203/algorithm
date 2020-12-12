def cal(num,index,numlist,a,b,c,d):
    global n,maxn,minn
    if index == n:
        maxn = max(num,maxn)
        minn = min(num,minn)
        return
    else:
        if a:
            cal(num+numlist[index],index+1,numlist,a-1,b,c,d)
        if b:
            cal(num-numlist[index],index+1,numlist,a,b-1,c,d)
        if c:
            cal(num*numlist[index],index+1,numlist,a,b,c-1,d)
        if d:
            cal(int(num/numlist[index]),index+1,numlist,a,b,c,d-1)




n = int(input())
maxn = -1000000000
minn = 1000000000
numlist = list(map(int,input().split(' ')))
a,b,c,d = map(int, input().split(' '))

cal(numlist[0],1,numlist,a,b,c,d)
print(maxn)
print(minn)
