from collections import defaultdict
n,m = map(int, input().split())

d = defaultdict(set)
num_list = [0 for _ in range(n+1)]

for _ in range(m):
    f_num, n_num = map(int,input().split())
    d[f_num].add(n_num)
    num_list[n_num] += 1

final_list = []

for i in range(1,n+1):
    if (str(i) not in final_list) and (num_list[i] == 0):
        final_list.extend(str(i))

        for j in range(len(d[i])):
            list_d = list(d[i])
            num_list[list_d[j]] -= 1

            for k in range(len(list_d)):
                if (list_d[k] not in final_list) and (num_list[list_d[k]] == 0):
                    final_list.extend(str(list_d[k]))

print(" ".join(final_list))