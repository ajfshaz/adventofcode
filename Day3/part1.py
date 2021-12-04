# Gamma rate is the most common bit 
# Epsilon rate is the least common bit

gammaBinary = ''
gammaDec = 0
epsilonBinary = ''
epsilonDec = 0
powerConsumption = 0
splitBits = []

def GetInputList():
    global inputList
    with open('input.txt') as input:
        inputList = list(map(str, input.readlines()))
    return

def SplitBits():
    global splitBits
    listOfBits = [""] * 13
    for binaryValue in inputList:
        for x in range(len(binaryValue)):
            listOfBits[x] = listOfBits[x] + binaryValue[x]
    splitBits = listOfBits
    return

def GetGammaAndEpsilonRate():
    global gammaBinary, gammaDec, epsilonBinary, epsilonDec
    for bit in splitBits:
        gammaBinary = gammaBinary + max(set(bit), key=bit.count)
        epsilonBinary = epsilonBinary + min(set(bit), key=bit.count)
    gammaDec = gammaDec = int(gammaBinary,2)
    epsilonDec = int(epsilonBinary, 2)
    return

def CalculatePowerConsumption():
    global powerConsumption
    powerConsumption = gammaDec * epsilonDec
    return

def main():
    GetInputList()
    SplitBits()
    GetGammaAndEpsilonRate()
    CalculatePowerConsumption()
    print(powerConsumption)

    return
    
main()