# lifeSupportRating =  O2GeneratorRating * CO2ScrubberRating
# O2GeneratorRating = Most common value of each bit
# CO2ScrubberRating = Least common value of each bit

def get_input():
    global inputList
    with open('input.txt') as input:
        inputList = list(map(str, input.readlines()))
    return

def get_most_common_bit(listOfBits, position):
    tempBin = ""
    for eachBit in listOfBits:
        tempBin = tempBin + eachBit[position]
    maxBitValue = max(set(tempBin), key=tempBin.count)
    minBitValue = min(set(tempBin), key=tempBin.count)
    if(maxBitValue == minBitValue):
        return 1
    else:
        return maxBitValue

def get_least_common_bit(listOfBits, position):
    tempBin = ""
    for eachBit in listOfBits:
        tempBin = tempBin + eachBit[position]
    maxBitValue = max(set(tempBin), key=tempBin.count)
    minBitValue = min(set(tempBin), key=tempBin.count)
    if(maxBitValue == minBitValue):
        return 0
    else:
        return minBitValue

def remove_bit_values(listOfBits, bitValueToRemove, position):
    newList = []
    for eachBit in listOfBits:
        if(int(eachBit[position]) ==  int(bitValueToRemove)):
            newList.append(eachBit)
        else:
            continue
    return newList

def get_O2_Generator_Rating():
    listOfBits = inputList
    lengthOfBits = len(listOfBits[0])    
    for x in range(lengthOfBits):
        bitValue = get_most_common_bit(listOfBits, x)
        if(int(bitValue) == 1):
            bitValueToRemove = 0
        else:
            bitValueToRemove = 1
        listOfBits = remove_bit_values(listOfBits, bitValueToRemove, x)
        if(len(listOfBits) == 1):
            break      
    O2GeneratorRate= int(listOfBits[0],2)
    return O2GeneratorRate

def get_cO2_scrubber_rating():
    listOfBits = inputList
    lengthOfBits = len(listOfBits[0])    
    for x in range(lengthOfBits):
        bitValue = get_least_common_bit(listOfBits, x)
        if(int(bitValue) == 1):
            bitValueToRemove = 0
        else:
            bitValueToRemove = 1
        listOfBits = remove_bit_values(listOfBits, bitValueToRemove, x)
        if(len(listOfBits) == 1):
            break      
    O2GeneratorRate= int(listOfBits[0],2)
    return O2GeneratorRate

def main():
    get_input()
    o2Rate = get_O2_Generator_Rating()
    print("The O2 rating is:", o2Rate)
    CO2Rate = get_cO2_scrubber_rating()
    print("The CO2 rating is:", CO2Rate)
    lifeSupportRating = o2Rate * CO2Rate
    print("The life support rating is:", lifeSupportRating)


    return
    
main()