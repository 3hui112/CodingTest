def solution(num_str):
    num = list(map(int, list(num_str)))
    sum = 0
    
    for i in range(len(num)):
        sum += num[i]
    
    return sum
