# Gamma rate is the most common bit 
# Epsilon rate is the least common bit

class HeightMapScanner():
    totalXPoints = 0
    totalYPoints = 0 


def get_input_list():
    global inputList
    with open('input.txt') as input:
        inputList = list(map(str, input.readlines()))
    return


def main():
    get_input_list()
    print(inputList[0])
    return
    
main()