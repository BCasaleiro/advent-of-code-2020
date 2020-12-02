import time
from pathlib import Path
from typing import Any


def load_input() -> str:
    with Path('input.txt').open('r') as input_file:
        text_input = input_file.read()

    return text_input


def first_part(text_input: str) -> int:
    raw_lines = text_input.splitlines()

    invalid_password_count = 0
    for line in raw_lines:
        rules, raw_character, password = line.split(' ')
        min_count, max_count = (int(count) for count in rules.split('-'))
        character = raw_character.strip(':')

        characher_count = password.count(character)
        if max_count < characher_count or characher_count < min_count:
            invalid_password_count += 1

    return invalid_password_count


def second_part(text_input: str) -> Any:
    raw_lines = text_input.splitlines()

    valid_password_count = 0
    for line in raw_lines:
        rules, raw_character, password = line.split(' ')
        first_position, second_position = (int(position) - 1 for position in rules.split('-'))
        character = raw_character.strip(':')

        if (password[first_position] == character and password[second_position] != character) \
                or (password[first_position] != character and password[second_position] == character):
            valid_password_count += 1

    return valid_password_count


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
