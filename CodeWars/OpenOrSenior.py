def open_or_senior(data):
    result = []
    for member in data:
        result.append('Senior' if member[0] >= 55 and member[1] > 7 else 'Open')

    return result

    # return ["Senior" if age >= 55 and handicap >= 8 else "Open" for (age, handicap) in data]