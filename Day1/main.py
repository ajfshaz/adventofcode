def PartOne():
    depthMeasurementIncreaseCounter = 0
    with open('input.txt') as input:
        numbers = list(map(int, input.readlines()))
    previousNumber = numbers[0]
    for currentNumber in numbers:
        if(currentNumber > previousNumber):
            depthMeasurementIncreaseCounter = depthMeasurementIncreaseCounter + 1
        previousNumber = currentNumber
    print("The answer for part 1 : " + str(depthMeasurementIncreaseCounter))

def PartTwo():
    depthMeasurementIncreaseCounter = 0
    with open('input.txt') as input:
        numbers = list(map(int, input.readlines()))
    i = 0
    lengthOfNumbers = len(numbers)
    while (i < lengthOfNumbers-3):
        aNumOne = numbers[i]
        aNumTwo = numbers[i+1]
        aNumThree = numbers[i+2]

        bNumOne = numbers[i+1]
        bNumTwo = numbers[i+2]
        bNumThree = numbers[i+3]
        
        alphaTuple = aNumOne + aNumTwo + aNumThree
        betaTuple = bNumOne + bNumTwo + bNumThree

        if(betaTuple > alphaTuple):
            depthMeasurementIncreaseCounter = depthMeasurementIncreaseCounter + 1
        i += 1
    print("The answer for part 2 : " + str(depthMeasurementIncreaseCounter))

PartOne()
PartTwo()
