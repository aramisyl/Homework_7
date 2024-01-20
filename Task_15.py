def divisors(n):
    result = []
    for i in range(1, n//2 + 1):
        if n % i == 0:
            result.append(i)
    result.append(n)
    return set(result)

def test_1():
    result = divisors(12)
    assert result == {1, 2, 3, 4, 6, 12}