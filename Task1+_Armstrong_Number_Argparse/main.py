import argparse


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


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description="Finds which number is Armstong's number in range and calculates sum of them.")
    parser.add_argument('start', type=int,
                        help="Number from where range will start")
    parser.add_argument('end', type=int, help="Number where range will end")
    args = parser.parse_args()

start = args.start
end = args.end
print(sumOfArmstrong(isArmstrong(start, end)))
