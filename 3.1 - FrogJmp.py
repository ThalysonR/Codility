def solution(X, Y, D):
    pulos, resto = divmod((Y - X), D)
    return pulos if resto <= 0 else pulos + 1
