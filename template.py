import time
from pathlib import Path
from typing import Any


def load_input() -> str:
    with Path('input.txt').open('r') as input_file:
        text_input = input_file.read()

    return text_input


def first_part(text_input: str) -> Any:
    pass


def second_part(text_input: str) -> Any:
    pass


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
