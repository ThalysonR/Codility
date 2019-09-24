def solution(A):
    sA = sorted(A)
    if len(A) == 0:
        return 1
    elif sA[-1:][0] == len(A):
        return len(A) + 1
    elif sA[0] != 1:
        return 1
    else:
        for i in range(len(sA)):
            if sA[i + 1] - sA[i] > 1:
                return sA[i] + 1
    return 0

