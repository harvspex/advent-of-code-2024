
def find_next(string: str, start: int, *args: str):
    next_indices = {}

    for arg in args:
        next_index = string.find(arg, start)

        if next_index != -1:
            next_indices[next_index] = arg

    sorted_indices = sorted(next_indices.items())

    return sorted_indices[0] if len(sorted_indices) > 0 else (None, None)

test = 'ioarstneio'

a, b = find_next(test, 1, 'x')

print(a, b)