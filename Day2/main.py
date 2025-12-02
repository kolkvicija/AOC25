with open("input.txt") as file:
    f = file.read()
all_ranges = f.split(",")

def part_one():
    invalid_ids = 0

    for i in all_ranges:
        rang = i.split("-")
        start = rang[0]
        end = rang[1]

        for num in range(int(start), int(end)+1):
            l = len(str(num))
            if l % 2 == 0:
                first = str(num)[0:l//2]
                second = str(num)[l//2:l]
                if first == second:
                    invalid_ids += num

    print(invalid_ids)

def part_two():
    pass



if __name__ == "__main__":
    part_one()