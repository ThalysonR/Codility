def solution(N, A):
    counters = [0]*N
    maxCounter = 0
    maxCounterApplied = 0
    
    for X in A:
        if X <= N:
            if counters[X - 1] < maxCounterApplied:
                counters[X - 1] = maxCounterApplied
            counters[X - 1] = counters[X - 1] + 1
            maxCounter = maxCounter if maxCounter > counters[X - 1] else counters[X - 1]
        else:
            maxCounterApplied = maxCounter
        
    counters = [n if n >= maxCounterApplied else maxCounterApplied for n in counters]
    return counters
