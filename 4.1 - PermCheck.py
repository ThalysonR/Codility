def solution(A):
    sA = sorted(A)
    for i in range(1, max(sA[-1:][0], len(A)) + 1):
        if i != sA[i - 1]:
            return 0
    return 1
