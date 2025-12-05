with open("input.txt") as file:
    f = file.readlines()

ranges = []
indexes = []

def part_one():
    counter = 0
    fl = 0

    for line in f:
        if "-" in line:

            l, r = line.split("-")
            ranges.append((int(l), int(r)))
        else:
            line = line.replace("\n", "").replace("\r", "")
            if line:
                indexes.append(int(line))


    for idx in indexes:
        fl = 0
        for rang in ranges:
            start, end = rang[0], rang[1]
            if start <= idx <= end:
                fl = 1
        if fl: counter += 1

    print(counter)

if __name__ == "__main__":
    part_one()