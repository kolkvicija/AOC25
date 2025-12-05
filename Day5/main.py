with open("input.txt") as file:
    f = file.readlines()

ranges = []
indexes = []

for line in f:
    if "-" in line:

        l, r = line.split("-")
        ranges.append((int(l), int(r)))
    else:
        line = line.replace("\n", "").replace("\r", "")
        if line:
            indexes.append(int(line))


def part_one():
    counter = 0
    fl = 0

    for idx in indexes:
        fl = 0
        for rang in ranges:
            start, end = rang[0], rang[1]
            if start <= idx <= end:
                fl = 1
        if fl: counter += 1

    print(counter)


def part_two():
    total = 0
    ranges.sort(key=lambda x: x[0])

    m = []
    for start, end in ranges:

        if not m:
            m.append((start, end))

        else:
            last_start, last_end = m[-1]
            if start <= last_end + 1:
                m[-1] = (last_start, max(last_end, end))
            else:
                m.append((start, end))

    total = sum(end - start + 1 for start, end in m)

    return total


if __name__ == "__main__":
    # part_one()
    print(part_two())
