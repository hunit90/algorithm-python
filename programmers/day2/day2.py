def solution(code):
    answer = ''
    mode = 0

    for idx in range(len(code)):
        if code[idx] == '1':
            mode = 1 - mode
        elif mode == 0 and idx % 2 == 0:
            answer += code[idx]
        elif mode == 1 and idx % 2 == 1:
            answer += code[idx]

    return answer if answwer else 'EMPTY'