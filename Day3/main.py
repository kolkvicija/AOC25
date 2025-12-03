with open("input.txt") as file:
    f = file.readlines()


def main(n):
    total_joltage = 0

    for entry in f:
        entry = entry.rstrip("\r\n")
        keep = n
        rem = len(entry) - keep
        s = []
        for d in entry:
            while s and rem > 0 and s[-1] < d:
                s.pop()
                rem -= 1
            s.append(d)

        jolts = int("".join(s[:keep]))
        total_joltage += jolts

    print(total_joltage)


if __name__ == "__main__":
    main(2)
    main(12)
