def solution(X, A):
    nDict = {}
    nCount = 0
    for i in range(len(A)):
        n = nDict.get(A[i], 0)
        if n == 0:
            nCount = nCount + 1
            nDict[A[i]] = n + 1
        if nCount == X:
            return i
    return 0
