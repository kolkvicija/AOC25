"""
OLD CODE: 

    def part_one():
    total_joltage = 0

    for entry in f:
        entry = entry.rstrip("\r\n")
        max_jolts = 0
        for i in range(len(entry)):
            for j in range(i + 1, len(entry)):
                jolts = int(entry[i] + entry[j])
                if jolts > max_jolts:
                    max_jolts = jolts
        total_joltage += max_jolts

    return total_joltage


def part_two():
    total_joltage = 0

    for entry in f:
        entry = entry.rstrip("\r\n")
        keep = 12
        rem = len(entry) - keep
        s = []
        for d in entry:
            while s and rem > 0 and s[-1] < d:
                s.pop()
                rem -= 1
            s.append(d)
        jolts_digits = s[:keep]
        jolts = int("".join(jolts_digits))
        total_joltage += jolts

    print(total_joltage)
"""