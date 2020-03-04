from collections import defaultdict

def solution(clothes):

    dict_clothes = defaultdict(set)
    for cloth in clothes:
        print(cloth)
        value = cloth[0]
        key = cloth[1]
        dict_clothes[key].add(value)
        dict_clothes[key].add("None")

    len_dict = len(dict_clothes)
    answer = 1
    print(list(dict_clothes.keys())[0])
    for i in list(dict_clothes.keys()):
        size = len(list(dict_clothes.get(i)))
        answer = answer*size
    return answer-1



clothes = [["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]

print(solution(clothes))