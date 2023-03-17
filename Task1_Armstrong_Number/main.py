

def isArmstrong(start, end):
    armstrongNumbers = []
    i = start
    while i <= end:
        numLength = len(str(i))
        digitSum = sum(int(digit) ** numLength for digit in str(i))
        if digitSum == i:
            armstrongNumbers.append(i)
        i += 1
    return armstrongNumbers


def sumOfArmstrong(n):
    if not n:
        return 0
    elif len(n) == 1:
        return n[0]
    else:
        return n[0] + sumOfArmstrong(n[1:])



print(sumOfArmstrong(isArmstrong(9, 10000)))
