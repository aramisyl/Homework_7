def polyndrome_list():
    return [i for i in range(1, 101) if str(i) == str(i)[::-1]]

print(polyndrome_list())