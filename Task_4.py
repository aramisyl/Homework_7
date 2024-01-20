def tuple_sum(values):
    sum = 0
    for item in list(values):
        if item % 2 == 0:
            sum += item
        else:
            sum += 0
    return sum

def test_1():
    result = tuple_sum((1, 2, 3, 4))
    assert result == 6

def test_2():
    result = tuple_sum((1, 7, 3, 9))
    assert result == 0

def test_3():
    result = tuple_sum((1, ))
    assert result == 0

def test_4():
    result = tuple_sum((2, ))
    assert result == 2