def solution(A):
    nDict = {}
    sA = sorted(A)
    for n in sA:
        nCount = nDict.get(n,0)
        if nCount > 0:
            return 0
        nDict[n] = nCount + 1
    if len(A) == sA[-1:][0]:
        return 1
    else:
        return 0
