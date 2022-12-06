import os
import string

# [J]             [F] [M]            
# [Z] [F]     [G] [Q] [F]            
# [G] [P]     [H] [Z] [S] [Q]        
# [V] [W] [Z] [P] [D] [G] [P]        
# [T] [D] [S] [Z] [N] [W] [B] [N]    
# [D] [M] [R] [J] [J] [P] [V] [P] [J]
# [B] [R] [C] [T] [C] [V] [C] [B] [P]
# [N] [S] [V] [R] [T] [N] [G] [Z] [W]
#  1   2   3   4   5   6   7   8   9 
def main():
    path = os.path.dirname(os.path.abspath(__file__)) + "/data.txt"
    with open(path) as file:
        commands = []
        for line in file: 
            commands.append([int(digit) for digit in line.split() if digit.isdigit()])

    print(part1(commands))
    print(part2(commands))

def part1(commands):
    containers = getContainers()
    for command in commands:
        move, frm, to = command[0], command[1], command[2]

        fromBlocks = containers[frm]    
        toBlocks = containers[to]
        count = 0
        while move > count:
            block = fromBlocks.pop()
            toBlocks.append(block)
            count += 1

    result = ""
    for block in containers.values():
        result += block.pop()

    return result

def part2(commands):
    containers = getContainers()
    for command in commands:
        move, frm, to = command[0], command[1], command[2]
        fromBlocks = containers[frm]    
        toBlocks = containers[to]

        containers[to] = toBlocks + fromBlocks[len(fromBlocks) - move:]
        containers[frm] = fromBlocks[:len(fromBlocks) - move]
      
    result = ""
    for block in containers.values():
        result += block.pop()

    return result

def getContainers():
    return {
        1: ["N", "B", "D", "T", "V", "G", "Z", "J"],
        2: ["S", "R", "M", "D", "W", "P", "F"],
        3: ["V", "C", "R", "S", "Z"],
        4: ["R", "T", "J", "Z", "P", "H", "G"],
        5: ["T", "C", "J", "N", "D", "Z", "Q", "F"],
        6: ["N", "V", "P", "W", "G", "S", "F", "M"],
        7: ["G", "C", "V", "B", "P", "Q"],
        8: ["Z", "B", "P", "N"],
        9: ["W", "P", "J"]
    }

if __name__=="__main__":
    main()
