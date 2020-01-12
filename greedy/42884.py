def solution(routes):
    routes.sort(key=lambda x: x[0])
    result = 1

    area_start = routes[0][0]
    area_end = routes[0][1]

    for start,end in routes:
        if (start >= area_start) & ( start <= area_end):
            area_start = start
            area_end = min(end,area_end)

        else:
            result +=1
            area_start = start
            area_end = end

    return result

print(solution([[-20,15], [-14,-5], [-18,-13], [-5,-3]]))


"""
참조 https://blog.naver.com/jjys9047/221686814646
"""