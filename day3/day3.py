import os
import string

def main():
    path = os.path.dirname(os.path.abspath(__file__)) + "/data.txt"
    with open(path) as file:
        items = [line for line in file.read().splitlines()]

    print(part1(items))
    print(part2(items))

def part1(items):
    alphabetPriority = alphabet()
    result = 0
    for item in items:
        halfSize = len(item) // 2
        leftPart =  set(item[:halfSize])
        rightPart =  set(item[halfSize:])

        repeating = leftPart.intersection(rightPart).pop()
        result += alphabetPriority[repeating]

    return result

def part2(items):
    alphabetPriority = alphabet()
    groupedElfs = []
    step = 3
    for i in range(0, len(items), step):
        groupedElfs.append(items[i:i + step])

    result = 0
    for elf in groupedElfs:
        item1, item2, item3 = set(elf[0]), set(elf[1]), set(elf[2]) 
        repeating = item1.intersection(item2, item3).pop()
        result += alphabetPriority[repeating]
    
    return result

def alphabet():
    letters = {}
    for index, letter in enumerate(string.ascii_letters):
        letters[letter] = index + 1
    return letters

if __name__=="__main__":
    main()