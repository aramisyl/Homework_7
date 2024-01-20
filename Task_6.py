def pair_to_dict(values):
    if len(values) == 0:
        return 'Invalid input'
    source = values.split(", ")
    source_with_items = []
    for i in source:
        item = i.split(" ")
        source_with_items.append(item)
    return {k:int(v) for k, v in source_with_items}


def test_1():
    result = pair_to_dict("a 1, b 2, c 3")
    assert result == {'a': 1, 'b': 2, 'c': 3}

def test_2():
    result = pair_to_dict("a 1")
    assert result == {'a': 1}

def test_3():
    result = pair_to_dict("")
    assert result == 'Invalid input'