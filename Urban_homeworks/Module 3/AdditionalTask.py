def calculate_structure_sum(data):
    if isinstance(data, int) or isinstance(data, float):
        return data

    if isinstance(data, str):
        return len(data)

    result = 0
    if isinstance(data, dict):
        for key, value in data.items():
            result += calculate_structure_sum(key)
            result += calculate_structure_sum(value)
    else:
        for item in data:
            result += calculate_structure_sum(item)

    return result


data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]

print(calculate_structure_sum(data_structure))
print(calculate_structure_sum(6))
print(calculate_structure_sum('some text'))
print(calculate_structure_sum(['some text', 20, {'my': 10, 'dict': 5}]))