horizontalValue = 0
depthValue = 0
aim = 0
inputList = []
finalValue = 0


# Forward x --> Adds x amount to the horizontal value AND Adds y amount to the depth value where y = aim * x
# Down x --> Adds x amount to the aim value (increases)
# Up x --> Subtracts x amount to the aim value (decreases)

def GetInputList():
    global inputList
    with open('input.txt') as input:
        inputList = list(map(str, input.readlines()))
    print(inputList[0])

def ProcessForwardValue(valueToAdd):
    AddToHorizontalValue(valueToAdd)
    IncreaseDepthValue(valueToAdd)
    return

def IncreaseDepthValue(valueToAdd):
    global depthValue
    calculatedDepthValue  = aim * valueToAdd
    depthValue = depthValue + calculatedDepthValue
    return

def AddToHorizontalValue(valueToAdd):
    global horizontalValue
    horizontalValue = horizontalValue + valueToAdd
    return

def AddToAimValue(valueToAdd):
    global aim
    aim = aim + valueToAdd
    return

def SubtractFromAimValue(valueToRemove):
    global aim
    aim = aim - valueToRemove
    return

def CalculateValuesFromList():
    for value in inputList:
        splitValue = value.split(' ')
        print("test")
        if( splitValue[0] == 'forward'):
            ProcessForwardValue(int(splitValue[1]))
        elif(splitValue[0] == 'up'):
            AddToAimValue(int(splitValue[1]))
        elif(splitValue[0] == 'down'):
            SubtractFromAimValue(int(splitValue[1]))

def MultiplyFinalDepthAndHorizontalValue():
    global finalValue
    finalValue = horizontalValue * depthValue


def main():
    GetInputList()
    CalculateValuesFromList()
    MultiplyFinalDepthAndHorizontalValue()
    print(finalValue)
    
main()