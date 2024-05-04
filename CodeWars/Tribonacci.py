def tribonacci(signature, n):
    # if n < 3:
    #     [signature.pop(-1) for i in range(0, 3 - n)]
    # else:
    #     [signature.append(sum(signature[0 + i:])) for i in range(0, n - 3)]
    # return signature

    # res = signature[:n]
    # for i in range(n - 3): res.append(sum(res[-3:]))
    # return res

    [signature.append(sum(signature[0 + i:])) for i in range(0, n - 3)]
    return signature[:n]


print(tribonacci([1, 1, 1], 10))
print(tribonacci([1, 1, 1], 1))