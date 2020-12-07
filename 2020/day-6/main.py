from typing import List, Dict

def readGroupAnswersFromFile(fileName: str) -> List[List[str]]:
    allGroups: List[List[str]] = []

    with open("/Users/willwolf/Documents/Programming/advent-of-code/2020/day-6/" + fileName, mode='r') as inputFile:
        fileContent = inputFile.readlines()
        currentGroup: List[str] = []
        allGroups.append(currentGroup)

        for line in fileContent:
            line = line.strip()

            if line == '':
                currentGroup = []
                allGroups.append(currentGroup)
            else:
                currentGroup.append(line)

    return allGroups

def countUniqueAnswers(groupAnswers: List[str]) -> int:
    counts: Dict[str, int] = {}

    for person in groupAnswers:
        for answer in person:
            counts[answer] = 1

    return len(counts.keys())

fileName = input("Enter file to read from: ")
groups = readGroupAnswersFromFile(fileName)
totalCounts = sum(map(countUniqueAnswers, groups))

print("Total counts:", totalCounts)