def solution(price, money, count):
    result = min(0, money-sum(price*i for i in range(1,count+1)))
    return abs(result)
