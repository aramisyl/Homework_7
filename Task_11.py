import math
def create_dictionary():
    return {value: math.factorial(value) for value in range(1, 11)}

print(create_dictionary())