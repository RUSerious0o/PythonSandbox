with open('text.txt', 'r') as file:             # same result as: file = open('text.txt', 'r') / with file:
    # print(*file)
    for line in file:
        print(line, end='')
print(file.closed)
