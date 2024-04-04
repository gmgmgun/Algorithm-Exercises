def get_input():
    n = int(input())
    cases = []

    for _ in range(n):
        num_clothes = int(input())
        clothes = []

        for _ in range(num_clothes):
            cloth = input().split()
            clothes.append(tuple(cloth))

        cases.append(clothes)

    return cases


def count_outfit():
    cases = get_input()
    results = []
    
    for clothes in cases:
        cloth_map = {}
        
        for _, cloth_type in clothes:
            cloth_map[cloth_type] = cloth_map.get(cloth_type, 0) + 1

        combinations = 1
        
        for count in cloth_map.values():
            combinations *= (count + 1)

        results.append(combinations - 1)

    for result in results:
        print(result)


count_outfit()
