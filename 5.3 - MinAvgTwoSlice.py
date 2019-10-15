def solution(A, B, K):
    nA, modA = divmod(A, K)
    nB = B // K
    A1 = (nA if modA == 0 else nA + 1) * K
    B1 = nB * K
    intervalo = B1 - A1
    return (intervalo // K) + 1
