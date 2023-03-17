import argparse

if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument("testString", help="Enter a string which you want to be checked and value extracted")
    args = parser.parse_args()

    testString = args.testString

floatList = []
oddList = []
evenList = []

i = 0
while i < len(testString):
    if testString[i].isdigit() or testString[i] == '.':
        j = i + 1
        while j < len(testString) and (testString[j].isdigit() or testString[j] == '.'):
            j += 1
        value = testString[i:j]
        if '.' in value:
                floatValue = float(value)
                floatList.append(floatValue)
        else:
                intValue = int(value)
                if intValue % 2 == 0:
                    evenList.append(intValue)
                else:
                    oddList.append(intValue)
        i = j
    else:
        i += 1


print("Float List:", floatList)
print("Odd List:", oddList)
print("Even List:", evenList)

