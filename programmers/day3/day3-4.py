def solution(my_string, queries):
    result = list(my_string)
    
    for s, e in queries:
        result[s:e+1] = result[s:e+1][::-1]
    
    return ''.join(result)