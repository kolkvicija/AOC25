with open("input.txt") as file:
    f = file.readlines()

f = [line.rstrip("\n") for line in f]
entries = []

for item in f:
    entries.append(item.split())


def calc(it, op):
    n = 0
    if op == "+":
        n = sum(it)

    elif op == "*":
        n = 1
        for k in it:
            n *= k
    return n


def part_one():
    grand_total = 0

    for i in range(len(entries[0])):
        op = 0
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

        n = calc(nums, op)

        grand_total += n

    print(grand_total)


def part_two():

    nr = len(f)
    nc = max(len(row) for row in f)
    cols = []

    for i in range(nc):
        col = []
        for j in range(nr):
            if i < len(f[j]):
                col.append(f[j][i])
            else:
                col.append(' ')
        cols.append(col)

    grand_total = 0

    for idx in range(len(cols)):
        if cols[idx] == " ":
            idx += 1
            continue

        nums = []
        op = cols[idx][-1]

        for j in range(idx, len(cols)):
            col = cols[j]

            if all(c == ' ' for c in col):
                idx = j
                break

            add = ''.join(col[:-1]).strip()
            if add:
                nums.append(int(add))
        else:
            idx = len(cols)

        idx += 1
        n = calc(nums, op)
        grand_total += n

    print(grand_total)


if __name__ == "__main__":
    part_two()
