def getNumber(num): # 선천수 계산
    numString = str(num)
    sum = 0
    for i in numString:
        sum += int(i)
    if sum <= 22:
        return sum
    else:
        return getNumber(sum)