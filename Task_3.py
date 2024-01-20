def shortest_longest_tuple(values):
    shortest_word = values[0]
    longest_word = values[0]
    for item in values:
        if item > longest_word:
            longest_word = item
        if item < shortest_word:
            shortest_word = item
    return (shortest_word, longest_word)

print(shortest_longest_tuple(['один','два','тринадцать']))

def test_1():
    result = shortest_longest_tuple(['один','два','тринадцать'])
    assert result == ('два', 'тринадцать')

def test_2():
    result = shortest_longest_tuple(['один','один','четы'])
    assert result == ('один', 'четы')

def test_3():
    result = shortest_longest_tuple(['эксперт'])
    assert result == ('эксперт', 'эксперт')