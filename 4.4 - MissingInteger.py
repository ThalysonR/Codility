def solution(A):
    sA = sorted(A)
    maxA = sA[-1:][0]
    if maxA < 1:
        return 1
    minN = maxA
    for i in range(len(A) - 1):
        if minN > sA[i] + 1 and sA[i + 1] - sA[i] > 1:
            minN = sA[i] + 1
    return minN if minN < maxA else maxA + 1
