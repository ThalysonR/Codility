def solution(A):
    sA = sorted(A)
    smallest = 1
    for n in sA:
        if n == smallest:
            smallest += 1
    return smallest
