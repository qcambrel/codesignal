def sudoku2(grid):
    isvalid = []
    subgrids = [
        [row[:3] for row in grid[:3]],
        [row[3:6] for row in grid[:3]],
        [row[6:] for row in grid[:3]],
        [row[:3] for row in grid[3:6]],
        [row[3:6] for row in grid[3:6]],
        [row[6:] for row in grid[3:6]],
        [row[:3] for row in grid[6:]],
        [row[3:6] for row in grid[6:]],
        [row[6:] for row in grid[6:]]
    ]
    vectors = []
    for subgrid in subgrids:
        vectors.append(sum(subgrid, []))
    for row in grid:
        vectors.append(row)
    grid_columns = list(zip(*grid))
    for column in grid_columns:
        vectors.append(column)
    for vector in vectors:
        isvalid.append(
            len(list(filter(lambda x: x != ".", vector))) == len(set(filter(lambda x: x != ".", vector)))
        )
    return min(isvalid)

