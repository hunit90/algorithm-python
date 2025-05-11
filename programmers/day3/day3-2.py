def solution(arr, queries):
    result = arr.copy()
    
    for s, e, k in queries:
        for i in range(s, e + 1):
            if i % k == 0:
                result[i] += 1
    
    return result