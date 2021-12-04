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
    i = 0
    tempBin = ""
    for binaryValue in inputList:
        tempBin = tempBin + binaryValue[i]
    bitValue = max(set(tempBin), key=tempBin.count)
    print(bitValue)
    return

def GetGammaAndEpsilonRate():
    global gammaBinary, gammaDec, epsilonBinary, epsilonDec
    for bit in splitBits:
        gammaBinary = gammaBinary + max(set(bit), key=bit.count)
        epsilonBinary = epsilonBinary + min(set(bit), key=bit.count)
    gammaDec = gammaDec = int(gammaBinary,2)
    epsilonDec = int(epsilonBinary, 2)
    return


def main():
    GetInputList()
    SplitBits()

    return
    
main()