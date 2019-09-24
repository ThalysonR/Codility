def solution(A, K):
    new_A = A
    for i in range(K):
        new_A = new_A[-1:] + new_A[:-1]
    return new_A
