"""Robot"""

def main():
    """Robot"""
    line1 = input().split()
    n = int(line1[0])
    p_val = float(line1[1])

    grid = []
    for _ in range(n):
        grid.append([int(val) for val in input().split()])

    col_tiles = [0] * n
    col_points = [0] * n
    total_tiles = 0
    total_points = 0

    for row in grid:
        row_tiles = sum(1 for x in row if x > 0)
        row_points = sum(row)

        total_tiles += row_tiles
        total_points += row_points

        row_str = " ".join(str(x) for x in row)
        print(f"{row_str} {row_tiles} {row_points}")

        for j in range(n):
            if row[j] > 0:
                col_tiles[j] += 1
            col_points[j] += row[j]

    print(" ".join(str(x) for x in col_tiles))
    print(" ".join(str(x) for x in col_points))
    print(f"{total_tiles} {total_points} {total_points * p_val:.2f}")

main()
