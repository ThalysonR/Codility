def solution(A):
    nDict = {}
    for n in A:
        nDict[n] = nDict.get(n,0) + 1
    for n,nV in nDict.items():
        if nV % 2 == 1:
            return n;
