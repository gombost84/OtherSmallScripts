# https://projecteuler.net/problem=1

def multiplesOfThreeFive():

    multiplesOfThree = 333
    multiplesOfFive = 199
    multiplesOfFifteen = 66 * 15

    sum = 0
    currentNum = 0

    while True:
        divisibleByThree = (currentNum % 3 == 0)
        divisibleByFive = (currentNum % 5 == 0)

        if currentNum >= multiplesOfFive and currentNum >= multiplesOfThree:
            break
        elif divisibleByThree and currentNum < multiplesOfThree:
            sum += currentNum
        elif divisibleByFive and currentNum < multiplesOfFive:
            sum += currentNum

        currentNum += 1

    return sum - multiplesOfFifteen
        
    

print(multiplesOfThreeFive())