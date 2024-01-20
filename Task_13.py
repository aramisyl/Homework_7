def generate_3_and_5_divisible():
    return [value for value in range(1, 101) if value % 3 == 0 or value % 5 == 0]

print(generate_3_and_5_divisible())