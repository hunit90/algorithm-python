def solution(l, r):
    result = set()
    
    def generate_numbers(current, digits):
        if current > r:
            return
        if current >= l and current != 0:
            result.add(current)
        if digits > len(str(r)):
            return
        
        generate_numbers(current * 10, digits + 1)
        generate_numbers(current * 10 + 5, digits + 1)
    
    generate_numbers(0, 0)
    
    return sorted(result) if result else [-1]


print(solution(5,555))