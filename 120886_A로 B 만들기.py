def solution(before, after):
    answer = 0
    str_reversed = before[::-1]
    
    if str_reversed == after :
        answer = 1
    
    return answer
