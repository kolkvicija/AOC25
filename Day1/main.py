with open("input.txt") as file:
    f = file.read()

data = f.split("\n")
ticks = [x for x in range(0, 100)]


def part_one():
    counter = 0
    dial = 50

    for i in data:
        if i[0] == "R":
            dial += int(i[1:])
            if ticks[abs(dial) % 100] == 0:
                counter += 1

        if i[0] == "L":
            dial -= int(i[1:])
            if ticks[abs(dial) % 100] == 0:
                counter += 1

    return counter


def part_two():
    counter = 0
    dial = 50

    for i in data:
        direction = i[0]
        step = int(i[1:])

        if direction == "R":
            for j in range(step):
                dial = (dial + 1) % 100
                if dial == 0:
                    counter += 1

        if direction == "L":
            for j in range(step):
                dial = (dial - 1) % 100
                if dial == 0:
                    counter += 1

    return counter


# Primjer korište
if __name__ == "__main__":
    print("Part One - Old password: ", part_one())
    print("Part Two - New password: ", part_two())
