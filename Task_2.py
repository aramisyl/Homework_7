def tuple_multiplier(one, two):
    if len(one) == len(two):
        result = []
        for index in range(len(two)):
            result.append(one[index]*two[index])
        return tuple(result)
    if len(one) != len(two):
        return "Tuples have different length. Please check your input."


print(tuple_multiplier((1,2,3),(4,5,6)))
def test_1():
    result = tuple_multiplier((1,2,3),(4,5,6))
    assert result == (4, 10, 18)

def test_2():
    result = tuple_multiplier((3,),(4,))
    assert result == (12,)

def test_3():
    result = tuple_multiplier((3,),(4,5))
    assert result == "Tuples have different length. Please check your input."

