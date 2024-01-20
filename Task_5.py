def max_value_index(values):
    length = len(values)
    if length >= 2:
        max_index = 0
        max_value = 0
        for index in range(length - 1):
            if values[index] >= values[index + 1]:
                if values[index] >= max_value:
                    max_index = index
                    max_value = values[index]
        return f'Max value: {max_value}, max value index: {max_index}.'
    else:
        return 'There should be at least 2 elements in the tuple.'

def test_1():
    result = max_value_index((1, 8, 3, 756, 4, 45, 4))
    assert result == 'Max value: 756, max value index: 3.'

def test_2():
    result = max_value_index((13, 13))
    assert result == 'Max value: 13, max value index: 0.'

def test_3():
    result = max_value_index(())
    assert result == 'There should be at least 2 elements in the tuple.'