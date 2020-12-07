from typing import Callable, List, Dict

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

def countUniqueAnswers(groupAnswers: List[str], countingStrat: Callable[[List[str], Dict[str,int]], int]) -> int:
    counts: Dict[str, int] = {}

    for person in groupAnswers:
        for answer in person:
            if answer not in counts:
                counts[answer] = 0
            counts[answer] += 1

    return countingStrat(groupAnswers, counts)

'''
Counts the number of answers that had a yes within a group (Part 1)
'''
def countAnyAnswer(groupAnswers: List[str], answerCounts: Dict[str,int]) -> int:
    return len(answerCounts.keys())

'''
Counts the number of answers that everyone in a group answered yes (Part 2)
'''
def countAnswersThatAllAnswered(groupAnswers: List[str], answerCounts: Dict[str, int]) -> int:
    numUniformAnswers = 0

    for answerAndCount in answerCounts.items():
        if answerAndCount[1] == len(groupAnswers):
            numUniformAnswers += 1

    return numUniformAnswers

fileName = input("Enter file to read from: ")
groups = readGroupAnswersFromFile(fileName)
totalCounts = sum(map(lambda x: countUniqueAnswers(x, countAnswersThatAllAnswered), groups))

print("Total counts:", totalCounts)