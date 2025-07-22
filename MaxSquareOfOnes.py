from typing import List

def max_size(grid: List[List[int]]) -> int:
    r = len(grid) # rows count
    c = len(grid[0]) # columns count

    grid_result = [[0] * c for _ in range(r)] # our result-tracking, memoization

    # Left to right, top to bottom, tracking square sizes as we descend.

    # Base case is thus leftmost column and topmost row
    grid_result[0] = grid[0][:] # shallow copy is sufficient since the inner array only contains ints

    for i in range(1, r, 1):
        grid_result[i][0] = grid[i][0]

    max_square = 0

    # dynamic programming
    for y in range(1, r, 1):
        for x in range(1, c, 1):
            if grid[y][x] == 1:
                grid_result[y][x] = min([grid_result[y-1][x-1], grid_result[y][x-1], grid_result[y-1][x]]) + 1

                if max_square < grid_result[y][x]:
                    max_square = grid_result[y][x]
    
    # note that the result at each coordinate pair of grid_result is the maximum sidelength square that can be made starting from that cell as the bottom corner
    for row in grid_result:
        print(row)

    return max_square

def main():

    test_grid = [
        [1, 0, 1, 1, 1, 0, 0, 1, 1, 1, 0, 0, 1, 1, 0],
        [1, 1, 1, 0, 0, 1, 1, 1, 1, 0, 1, 1, 0, 0, 1],
        [0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0],
        [1, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1],
        [0, 1, 1, 1, 0, 1, 1, 1, 1, 0, 0, 1, 0, 1, 0],
    ]

    print(max_size(test_grid))

if __name__ == "__main__":
    main()
