def score(dice):
    result = [0, 0, 0, 0, 0, 0]
    for case in dice:
        result[case - 1] += 1

    return result[0] // 3 * 1000 + result[0] %3 * 100 + result[1] // 3 * 200 + result[2] // 3 * 300 + \
        result[3] // 3 * 400 + result[4] // 3 * 500 + result[4] % 3 * 50 + result[5] // 3 * 600


print(score( [5, 1, 3, 4, 1]))