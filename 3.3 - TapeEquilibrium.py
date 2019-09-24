def solution(A):
    mVal = abs(sum(A[:1]) - sum(A[1:]))
    lSum = 0
    rSum = sum(A)
    for i in range(len(A) -1):
        lSum = lSum + A[i]
        rSum = rSum - A[i]
        dif = abs(lSum - rSum)
        if dif < mVal:
            mVal = dif
    return mVal
