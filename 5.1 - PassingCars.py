def solution(A):
    cC = 0
    passing = 0
    for n in A:
        if n == 0:
            cC += 1
        else:
            passing += cC
            if passing > 1000000000:
                return -1
    return passing
