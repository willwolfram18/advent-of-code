from typing import List, Tuple

def readNumbersFromFile(fileName) -> List[int]:
    numbers: List[int] = []

    with open("/Users/willwolf/Documents/Programming/advent-of-code/2020/day-1/" + fileName, 'r') as inputFile:
        fileContent = inputFile.readlines()

        for line in fileContent:
            line = line.strip()

            numbers.append(int(line))

    return numbers

def findPairMaking2020(numbers: List[int]) -> List[int]:
    for i in range(len(numbers)):
        firstValue = numbers[i]

        for j in range(i + 1, len(numbers)):
            secondValue = numbers[j]
            prospect = [firstValue, secondValue]

            if sum(prospect) == 2020:
                return prospect

    raise Exception("Failed to find a pair with a total of 2020")

def findTipletsMaking2020(numbers: List[int]) -> List[int]:
    for i in range(len(numbers)):
        firstValue = numbers[i]

        for j in range(i + 1, len(numbers)):
            secondValue = numbers[j]

            for k in range(j + 1, len(numbers)):
                thirdValue = numbers[k]

                prospect = [firstValue, secondValue, thirdValue]

                if sum(prospect) == 2020:
                    return prospect

    raise Exception("Failed to find a triplet with a total of 2020")

def calculateProduct(numbers: List[int]) -> int:
    product = 1

    for i in numbers:
        product *= i

    return product

fileName = input("Enter file name: ")
numbers = readNumbersFromFile(fileName)
setOfNumbers = findTipletsMaking2020(numbers)

print("Found values ", setOfNumbers)
print("Product is ", calculateProduct(setOfNumbers))