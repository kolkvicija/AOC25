with open("input.txt") as file:
    f = file.readlines()


def part_one():
    total = 0
    el = [
        (-1, -1), (-1, 0), (-1, 1),
        (0, -1), (0, 1),
        (1, -1), (1, 0), (1, 1)
    ]

    rows = len(f)

    i_idx = 0
    while i_idx < rows:
        row = f[i_idx]
        cols = len(row)

        j_idx = 0
        while j_idx < cols:
            if row[j_idx] == "@":
                counter = 0

                for dx, dy in el:
                    nx = i_idx + dx
                    ny = j_idx + dy

                    if 0 <= nx < rows and 0 <= ny < cols:
                        if f[nx][ny] == "@":
                            counter += 1

                if counter < 4:
                    total += 1

            j_idx += 1
        i_idx += 1

    print(total)


def part_two():
    grid = [list(row) for row in f]
    total_removed = 0

    el = [
        (-1, -1), (-1, 0), (-1, 1),
        (0, -1), (0, 1),
        (1, -1), (1, 0), (1, 1)
    ]

    rows = len(grid)

    removed_in_step = True

    while removed_in_step:
        removed_in_step = False
        to_remove = []

        i_idx = 0
        while i_idx < rows:
            row = grid[i_idx]
            cols = len(row)

            j_idx = 0
            while j_idx < cols:
                if row[j_idx] == "@":
                    counter = 0
                    for dx, dy in el:
                        nx = i_idx + dx
                        ny = j_idx + dy

                        if 0 <= nx < rows and 0 <= ny < len(grid[nx]):
                            if grid[nx][ny] == "@":
                                counter += 1
                    if counter < 4:
                        to_remove.append((i_idx, j_idx))
                j_idx += 1
            i_idx += 1

        for i_idx, j_idx in to_remove:
            grid[i_idx][j_idx] = "."
            total_removed += 1
            removed_in_step = True

    print(total_removed)


if __name__ == "__main__":
    # part_one()
    part_two()
