import os
from functools import reduce

def main():
    elves = []
    path = os.path.dirname(os.path.abspath(__file__)) + "/data.txt"
    with open(path) as file:
        calories = []
        for line in file:
            formattedLine = line.strip()
            if formattedLine == "":
                elves.append(calories.copy())
                calories.clear()
            else:
                calories.append(int(formattedLine))
    
    print(solution1(elves))
    print(solution2(elves))


def solution1(elves):
    maxCalories = 0

    for elf in elves:
        temp = reduce(lambda x, y: x + y, elf)
        if maxCalories < temp:
            maxCalories = temp
    
    return maxCalories

def solution2(elves):
    caloriesSums = []

    for elf in elves:
        sumCalories = reduce(lambda x, y: x + y, elf)
        caloriesSums.append(sumCalories)

    # Тут не стал особо думать, просто остротировал массив всех сумм 
    # и взял последние три значения :D
    caloriesSums.sort()
    
    result = caloriesSums[-1] + caloriesSums[-2] + caloriesSums[-3]
    return result

if __name__=="__main__":
    main()
