def solution(A):
    sA = sorted(A)
    for i in range(len(A)):
        if sA[i] != i + 1:
            return i + 1
    return 1 if len(A) == 0 else i + 2
