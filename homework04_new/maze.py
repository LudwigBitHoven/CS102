from copy import deepcopy
from random import choice, randint
from typing import List, Optional, Tuple, Union

import pandas as pd


def create_grid(rows: int = 15, cols: int = 15) -> List[List[Union[str, int]]]:
    return [["■"] * cols for _ in range(rows)]


def remove_wall(
    grid: List[List[Union[str, int]]], coord: Tuple[int, int]
) -> List[List[Union[str, int]]]:
    y, x = coord
    way = choice(("D", "L"))
    if way == "L":
        if x > 1:
            grid[y][x - 1] = " "
        else:
            if y < len(grid) - 2:
                grid[y + 1][x] = " "
    else:
        if y < len(grid) - 2:
            grid[y + 1][x] = " "
        else:
            if x > 1:
                grid[y][x - 1] = " "
    return grid


def bin_tree_maze(
    rows: int = 15, cols: int = 15, random_exit: bool = True
) -> List[List[Union[str, int]]]:
    """

    :param rows:
    :param cols:
    :param random_exit:
    :return:
    """

    grid = create_grid(rows, cols)
    empty_cells = []
    for x, row in enumerate(grid):
        for y, _ in enumerate(row):
            if x % 2 == 1 and y % 2 == 1:
                grid[x][y] = " "
                empty_cells.append((x, y))

    # 1. выбрать любую клетку
    # 2. выбрать направление: наверх или направо.
    # Если в выбранном направлении следующая клетка лежит за границами поля,
    # выбрать второе возможное направление
    # 3. перейти в следующую клетку, сносим между клетками стену
    # 4. повторять 2-3 до тех пор, пока не будут пройдены все клетки

    # генерация входа и выхода
    for _, i in enumerate(empty_cells):
        grid = remove_wall(grid, i)
    if random_exit:
        x_in, x_out = randint(0, rows - 1), randint(0, rows - 1)
        y_in = randint(0, cols - 1) if x_in in (0, rows - 1) else choice((0, cols - 1))
        y_out = randint(0, cols - 1) if x_out in (0, rows - 1) else choice((0, cols - 1))
    else:
        x_in, y_in = 0, cols - 2
        x_out, y_out = rows - 1, 1

    grid[x_in][y_in], grid[x_out][y_out] = "X", "X"

    return grid


def get_exits(grid: List[List[Union[str, int]]]) -> List[Tuple[int, int]]:
    """

    :param grid:
    :return:
    """

    y, x = len(grid), len(grid[0])
    return [(i, j) for i in range(y) for j in range(x) if "X" == grid[i][j]]


def make_step(grid: List[List[Union[str, int]]], k: int) -> List[List[Union[str, int]]]:
    """

    :param grid:
    :param k:
    :return:
    """

    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == k:
                if i - 1 >= 0 and grid[i - 1][j] == 0:
                    grid[i - 1][j] = k + 1
                if i + 1 < len(grid) and grid[i + 1][j] == 0:
                    grid[i + 1][j] = k + 1
                if j - 1 >= 0 and grid[i][j - 1] == 0:
                    grid[i][j - 1] = k + 1
                if j + 1 < len(grid[i]) and grid[i][j + 1] == 0:
                    grid[i][j + 1] = k + 1
    return grid


def shortest_path(grid, exit_coord: Tuple[int, int]) -> List[Tuple[int, ...]]:
    """
    :param grid:
    :param exit_coord:
    :return:
    """
    path = []
    path.append(tuple([exit_coord[0], exit_coord[1]]))
    k = grid[exit_coord[0]][exit_coord[1]]
    i = exit_coord[0]
    j = exit_coord[1]
    if grid[i][j] == k:
        if j - 1 >= 0 and j + 1 <= len(grid[0]) - 1:
            if grid[i][j - 1] == 1:
                path.append(tuple([i, j - 1]))
                return path
            if grid[i][j + 1] == 1:
                path.append(tuple([i, j + 1]))
                return path
        if i - 1 >= 0 and i + 1 <= len(grid) - 1:
            if grid[i - 1][j] == 1:
                path.append(tuple([i - 1, j]))
                return path
            if grid[i + 1][j] == 1:
                path.append(tuple([i + 1, j]))
                return path
    while k != 1:
        if grid[i][j] == k:
            if grid[i - 1][j] == k - 1:
                k -= 1
                i, j = i - 1, j
                path.append(tuple([i, j]))
            elif grid[i + 1][j] == k - 1:
                k -= 1
                i, j = i + 1, j
                path.append(tuple([i, j]))
            elif grid[i][j - 1] == k - 1:
                k -= 1
                i, j = i, j - 1
                path.append(tuple([i, j]))
            elif grid[i][j + 1] == k - 1:
                k -= 1
                i, j = i, j + 1
                path.append(tuple([i, j]))
    return path


def encircled_exit(grid: List[List[Union[str, int]]], coord: Tuple[int, int]) -> bool:
    """

    :param grid:
    :param coord:
    :return:
    """

    if coord[0] == 0 and grid[coord[0] + 1][coord[1]] != " ":
        return True
    if coord[0] == len(grid) - 1 and grid[coord[0] - 1][coord[1]] != " ":
        return True
    if coord[1] == 0 and grid[coord[0]][coord[1] + 1] != " ":
        return True
    if coord[1] == len(grid[0]) - 1 and grid[coord[0]][coord[1] - 1] != " ":
        return True
    return False


def solve_maze(grid: List[List[Union[str, int]]]):
    """
    :param grid:
    :return:
    """
    coord = get_exits(grid)
    if len(coord) == 1:
        return grid, coord[0]
    if not encircled_exit(grid, coord[0]) and not encircled_exit(grid, coord[1]):
        for x, row in enumerate(grid):
            for y, _ in enumerate(row):
                if grid[x][y] == " ":
                    grid[x][y] = 0
        grid[coord[0][0]][coord[0][1]], grid[coord[1][0]][coord[1][1]] = 1, 0
        k = 1
        while grid[coord[1][0]][coord[1][1]] == 0:
            grid = make_step(grid, k)
            k += 1
        path = shortest_path(grid, coord[1])
        for x, row in enumerate(grid):
            for y, _ in enumerate(row):
                if grid[x][y] != " " and grid[x][y] != "■":
                    grid[x][y] = " "
        return grid, path
    return grid, None


def add_path_to_grid(
    grid: List[List[Union[str, int]]], path: Optional[Union[Tuple[int, int], List[Tuple[int, int]]]]
) -> List[List[Union[str, int]]]:
    """
    :param grid:
    :param path:
    :return:
    """

    if path:
        for i, row in enumerate(grid):
            for j, _ in enumerate(row):
                if (i, j) in path:
                    grid[i][j] = "X"
    return grid


if __name__ == "__main__":
    print(pd.DataFrame(bin_tree_maze(15, 15)))
    GRID = bin_tree_maze(15, 15)
    print(pd.DataFrame(GRID))
    _, PATH = solve_maze(GRID)
    MAZE = add_path_to_grid(GRID, PATH)
    print(pd.DataFrame(MAZE))