with open("input.txt") as file:
    f = file.readlines()

f = [line.rstrip("\n") for line in f]
entries = []

for item in f:
    entries.append(item.split())


def part_one():
    grand_total = 0
    idx = 0
    for i in range(len(entries[0])):

        op = 0
        n = 0
        nums = []
        for j in range(len(entries)):
            add = entries[j][i]

            if add.isdigit():
                add = int(add)
                nums.append(add)
            else:
                op = add
                continue

        if not nums:
            continue

        if op == "+":

            n = sum(nums)

        elif op == "*":
            n = 1
            for k in nums:
                n *= k

        grand_total += n

    print(grand_total)


if __name__ == "__main__":
    part_one()
