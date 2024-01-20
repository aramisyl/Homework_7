def tuple_min_max(a):
    if len(a) > 1:
        result = sorted(a)
        return (result[0], result[-1])
    if len(a) == 1:
        result = a[0]
        return (result, result)
    else:
        return 'Not possible to calculate'

def test_1():
    result = tuple_min_max([])
    assert result == 'Not possible to calculate'

def test_2():
    result = tuple_min_max([300])
    assert result == (300, 300)

def test_3():
    result = tuple_min_max([4, 5, 7, 23, 645, 1, 0])
    assert result == (0, 645)