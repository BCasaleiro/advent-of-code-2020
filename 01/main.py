import time
from pathlib import Path


def load_input() -> str:
    with Path('input.txt').open('r') as input_file:
        text_input = input_file.read()

    return text_input


def first_part(text_input: str) -> int:
    expense_list = [int(expense) for expense in text_input.splitlines()]
    for expense in expense_list:
        val = 2020 - expense

        if val in expense_list:
            return expense * val


def second_part(text_input: str) -> int:
    expense_list = [int(expense) for expense in text_input.splitlines()]
    n_expenses = len(expense_list)

    expense_sum = {}
    for index, expense in enumerate(expense_list):
        for i in range(index + 1, n_expenses):
            val = expense + expense_list[i]

            expense_sum[val] = (expense, expense_list[i])

    for pair_sum, expense_pair in expense_sum.items():
        val = 2020 - pair_sum

        if val in expense_list:
            return val * expense_pair[0] * expense_pair[1]


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
