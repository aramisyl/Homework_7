def is_part(one, two):
    if len(one) <= len(two):
        if one.issubset(two):
            return "Да"
        else:
            return "Нет"
    elif len(one) > len(two):
        if two.issubset(one):
            return "Да"
        else:
            return "Нет"

def test_1():
    result = is_part({1,2,3}, {1,2,3,4,5})
    assert result == "Да"


def test_2():
    result = is_part({1,2,3,4,5}, {2,3,4})
    assert result == "Да"

def test_3():
    result = is_part({11,12,13}, {1,2,3,4,5})
    assert result == "Нет"

def test_4():
    result = is_part({1,2,3,4,5}, {11,12,13})
    assert result == "Нет"