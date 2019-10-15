def solution(S, P, Q):
    impact_factor = {'A': 1, 'C': 2, 'G': 3, 'T': 4}
    gSum = [[0] * 4]
    for k in range(1, len(S) + 1):
        gSum.append(gSum[k - 1][:])
        index = impact_factor[S[k-1]] - 1
        gSum[k][index] += 1
    result = []
    for i in range(len(P)):
        for j in range(4):
            if gSum[Q[i] + 1][j] - gSum[P[i]][j] > 0 or j == 3:
                result.append(j + 1)
                break
                
    return result

