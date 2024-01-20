def all_actions(one, two):
    union = one | two
    intersection = one &  two
    diff = one - two
    simmetric_diff = one ^ two
    print(f'Объединение {union}')
    print(f'Пересечение {intersection}')
    print(f'Разность {diff}')
    print(f'Симметрическая разность {simmetric_diff}')

print(all_actions({1,2,3,4}, {3,4,5,6}))