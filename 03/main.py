import time
from pathlib import Path
from typing import List


def load_input() -> str:
    with Path('input.txt').open('r') as input_file:
        text_input = input_file.read()

    return text_input


def transverse_forest(map_lines: List[str], right_move: int, down_move: int) -> int:
    x, y = 0, 0
    map_width = len(map_lines[0])
    map_height = len(map_lines)

    tree_count = 0
    while y < map_height - 1:
        x = (x + right_move) % map_width
        y += down_move

        if map_lines[y][x] == '#':
            tree_count += 1

    return tree_count


def first_part(text_input: str) -> int:
    map_lines = text_input.splitlines()

    return transverse_forest(map_lines, 3, 1)


def second_part(text_input: str) -> int:
    combinations = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
    map_lines = text_input.splitlines()

    mul = 1
    for comb in combinations:
        mul *= transverse_forest(map_lines, comb[0], comb[1])

    return mul


def main() -> None:
    text_input = load_input()

    start_time = time.time()
    answer = first_part(text_input)
    delta_time = round(time.time() - start_time, 4)
    print(f"[first-part] Fount it, {answer}! (took {delta_time}s)")

    start_time = time.time()
    answer = second_part(text_input)
    delta_time = round(time.time() - start_time, 4)
    print(f"[second-part] Fount it, {answer}! (took {delta_time}s)")


if __name__ == "__main__":
    main()
