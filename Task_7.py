def value_by_key(dictionary, key):
    if key in dictionary.keys():
        return dictionary[key]
    else:
        return 'Ключ не найден'

def test_1():
    result = value_by_key({'a':1, 'b': 2, 'c': 3}, "b")
    assert result == 2


def test_2():
    result = value_by_key({'a':1, 'b': 2, 'c': 3}, "с")
    assert result == 'Ключ не найден'
    