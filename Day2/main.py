with open("input.txt") as file:
    f = file.read()
all_ranges = f.split(",")


def part_one():
    invalid_ids = 0

    for i in all_ranges:
        rang = i.split("-")
        start = rang[0]
        end = rang[1]

        for num in range(int(start), int(end) + 1):
            length = len(str(num))
            if length % 2 == 0:
                first = str(num)[0:length // 2]
                second = str(num)[length // 2:length]
                if first == second:
                    invalid_ids += num

    print(invalid_ids)


def part_two():
    def is_repeating_pattern(number):
        s = str(number)
        n = len(s)
        for x in range(1, n // 2 + 1):
            if n % x == 0:
                if s[:x] * (n // x) == s:
                    return True
        return False

    invalid_ids = 0

    for i in all_ranges:
        rang = i.split("-")
        start = int(rang[0])
        end = int(rang[1])

        for num in range(start, end + 1):
            if is_repeating_pattern(num):
                invalid_ids += num

    print(invalid_ids)


if __name__ == "__main__":
    #part_one()
    part_two()
