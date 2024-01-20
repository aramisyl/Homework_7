def diff_with_string(input):
    alphabet = {'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w',
                'x', 'y', 'z'}
    characters_to_strip = ".,?!/\[]{}`~@#$%^&*()"
    input_value = set(input.strip(characters_to_strip).lower())
    return alphabet - input_value

print(diff_with_string("Hello World!"))