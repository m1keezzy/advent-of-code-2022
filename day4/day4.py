import os

def main():
    pairs = []
    path = os.path.dirname(os.path.abspath(__file__)) + "/data.txt"
    with open(path) as file:
        for line in file:
            pairs.append(line.strip().split(","))
    print(part1(pairs))
    print(part2(pairs))


def part1(pairs):
    result = 0
    for pair in pairs:
        firstElf, secondElf = getElfRange(pair)
        if len(firstElf) > len(secondElf):
            if secondElf.issubset(firstElf):
                result = result + 1
        else: 
             if firstElf.issubset(secondElf):
                result = result + 1  
    return result

def part2(pairs):
    result = 0
    for pair in pairs:
        firstElf, secondElf = getElfRange(pair)
        if len(firstElf) > len(secondElf):
            if any(item in secondElf for item in firstElf):
                result = result + 1
        else: 
            if any(item in firstElf for item in secondElf):
                result = result + 1
    return result

def getElfRange(pair): 
    firstElf = pair[0].split("-")
    startFirstElf, endFirstElf = int(firstElf[0]), int(firstElf[1]) + 1
    rangeFirstElf = set(range(startFirstElf, endFirstElf))

    secondElf = pair[1].split("-")
    startSecondElf, endSecondElf = int(secondElf[0]), int(secondElf[1]) + 1
    rangeSecondElf = set(range(startSecondElf, endSecondElf))
    return rangeFirstElf, rangeSecondElf    

if __name__=="__main__":
    main()