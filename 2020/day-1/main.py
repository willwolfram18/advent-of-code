from typing import List, Tuple

def readNumbersFromFile(fileName) -> List[int]:
    numbers: List[int] = []

    with open("/Users/willwolf/Documents/Programming/advent-of-code/2020/day-1/" + fileName, 'r') as inputFile:
        fileContent = inputFile.readlines()

        for line in fileContent:
            line = line.strip()

            numbers.append(int(line))

    return numbers

def findPairMaking2020(numbers: List[int]) -> Tuple[int, int]:
    for i in range(len(numbers)):
        firstValue = numbers[i]

        for j in range(i + 1, len(numbers)):
            secondValue = numbers[j]

            if firstValue + secondValue == 2020:
                return (firstValue, secondValue)

    raise Exception("Failed to find a pair with a total of 2020")

fileName = input("Enter file name: ")
numbers = readNumbersFromFile(fileName)
pairOfNumbers = findPairMaking2020(numbers)

print("Found values ", pairOfNumbers)
print("Product is ", pairOfNumbers[0] * pairOfNumbers[1])