horizontalValue = 0
depthValue = 0
inputList = []
finalValue = 0
# Forward x --> Adds x amount to the horizontal value
# Down x --> Adds x amount to the depth value
# Up x --> Subtracts x amount to the depth value

def GetInputList():
    global inputList
    with open('input.txt') as input:
        inputList = list(map(str, input.readlines()))
    print(inputList[0])

def AddToHorizontalValue(valueToAdd):
    global horizontalValue
    horizontalValue = horizontalValue + valueToAdd
    return

def AddToDepthValue(valueToAdd):
    global depthValue
    depthValue = depthValue + valueToAdd
    return

def SubtractFromDepthValue(valueToRemove):
    global depthValue
    depthValue = depthValue - valueToRemove
    return

def CalculateValuesFromList():
    for value in inputList:
        splitValue = value.split(' ')
        print("test")
        if( splitValue[0] == 'forward'):
            AddToHorizontalValue(int(splitValue[1]))
        elif(splitValue[0] == 'up'):
            AddToDepthValue(int(splitValue[1]))
        elif(splitValue[0] == 'down'):
            SubtractFromDepthValue(int(splitValue[1]))

def MultiplyFinalDepthAndHorizontalValue():
    global finalValue
    finalValue = horizontalValue * depthValue


def main():
    GetInputList()
    CalculateValuesFromList()
    MultiplyFinalDepthAndHorizontalValue()
    print(finalValue)
    
main()