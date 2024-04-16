# small parse numbers from string example
userInput = 'Some user input 1.255 and 2.33.55 .48 24,25.1'
for word in userInput.split(' '):
    result = ''
    hasDelimiter = False

    for letter in word:
        if not hasDelimiter:
            if letter == '.' or letter == ',':
                hasDelimiter = True
                if len(result) == 0:
                    result += '0'
                result += '.'

        if letter.isnumeric():
            result += letter
    if result != '':
        print(float(result))