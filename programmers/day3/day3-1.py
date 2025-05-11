def solution(arr, queries):
    result = []
    
    for s, e, k in queries:
        valid_nums = [num for num in arr[s:e+1] if num > k]
        
        result.append(min(valid_nums) if valid_nums else -1)
    
    return result