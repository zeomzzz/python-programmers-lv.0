def solution(numbers):
    answer = 0
    num_list = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    num_thr = ["zer", "one", "two", "thr", "fou", "fiv", "six", "sev", "eig", "nin"]
    tmp_list = []
    start = 0
    
    while True :
        tmp_num = numbers[start : start + 3]
        for i in num_thr :
            if tmp_num == i :
                tmp_list.append(num_thr.index(i))
                start += len(num_list[num_thr.index(i)])
        if start == len(numbers) :
            break
    
    for j in range(len(tmp_list)) :
        answer += tmp_list[j] * (10 ** (len(tmp_list) - (j + 1)))
            
    return answer
