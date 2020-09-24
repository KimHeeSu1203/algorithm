def solution(operations):
    queue = []
    for i in range(len(operations)):
        orderO, num = operations[i][0], int(operations[i][1:])
        if orderO == 'I':
            queue.append(num)
        elif (orderO == 'D') & (num == -1) & (len(queue) > 0):
            queue.pop(queue.index(min(queue)))
        elif (orderO == 'D') & (num == 1)  & (len(queue) > 0):
            queue.pop(queue.index(max(queue)))

    if len(queue) == 0:
        return [0,0]

    return [max(queue),min(queue)]

operations = ["I 16", "I -5643", "D -1", "D 1", "D 1", "I 123", "D -1"]
print(solution(operations))