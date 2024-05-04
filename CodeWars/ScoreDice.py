def score(dice):
    result = [0, 0, 0, 0, 0, 0]
    for case in dice:
        result[case - 1] += 1

    return result[0] // 3 * 1000 + result[0] %3 * 100 + result[1] // 3 * 200 + result[2] // 3 * 300 + \
        result[3] // 3 * 400 + result[4] // 3 * 500 + result[4] % 3 * 50 + result[5] // 3 * 600

    # score, data = 0, {1: (0, 100, 200, 1000, 1100, 1200),
    #                   2: (0, 0, 0, 200, 200, 200),
    #                   3: (0, 0, 0, 300, 300, 300),
    #                   4: (0, 0, 0, 400, 400, 400),
    #                   5: (0, 50, 100, 500, 550, 600),
    #                   6: (0, 0, 0, 600, 600, 600)}
    # for i in data:
    #     score += (data[i][dice.count(i)])
    # return score

print(score( [5, 1, 3, 4, 1]))