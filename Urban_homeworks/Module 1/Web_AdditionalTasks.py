def get_averages(grades = [], students = {}):
    if len(grades) != len(students):
        print("Ошибка ввода")
        return students

    students = sorted(students)
    result = {}
    for i in range(len(grades)):
        result[students[i]] = sum(grades[i]) / len(grades[i])

    return result


grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
print(get_averages(grades, students))