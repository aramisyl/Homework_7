
def divisors(n):
    result = []
    for i in range(1, n//2 + 1):
        if n % i == 0:
            result.append(i)
    result.append(n)
    return result

def generate_dictionary():
    return {value: divisors(value) for value in range(1, 11)}

print(generate_dictionary())
