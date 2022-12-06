import os

def main():
    path = os.path.dirname(os.path.abspath(__file__)) + "/data.txt"
    with open(path) as file:
        datastream = file.readline()
    print(part1(datastream))
    print(part2(datastream))

def part1(datastream):
    size = len(datastream)
    for i in range(size):
        if i + 4 > size:
            return -1 

        key = set(datastream[i:i + 4])
        if len(key) == 4:
            return i + 4
    return -1

def part2(datastream):
    size = len(datastream)
    for i in range(size):
        if i + 14 > size:
            return -1 
        
        key = set(datastream[i:i + 14])
        if len(key) == 14:
            return i + 14
    return -1

if __name__=="__main__":
    main()