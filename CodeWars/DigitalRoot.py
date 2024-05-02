def digital_root(n):
    def count_sum(temp):
        number = str(temp)
        sum_ = 0
        for digit in number:
            sum_ += int(digit)

        return sum_

    result = count_sum(n)
    while result > 10:
        result = count_sum(result)

    return result


print(digital_root(214332985))
print(digital_root(942))
print(digital_root(132189))
print(digital_root(493193))
