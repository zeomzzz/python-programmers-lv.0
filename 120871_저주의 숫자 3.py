# 3x 마을의 1 ~ 100 리스트 만들고 인덱스 이용하여 answer 반환

def solution(n):
    town_num = []
    i = 1
    
    while len(town_num) < 101 :
        if i % 3 != 0 :
            if i % 10 != 3 :
                if (i // 10) % 10 != 3 :
                    town_num.append(i)
                    i += 1
                else :
                    i += 1
            else :
                i += 1
        else :
            i += 1
        
    answer = town_num[n - 1]
    
    return answer
