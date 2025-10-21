from typing import Callable
import re

def generator_numbers(text: str):
    regex = " \\d+[.]\\d{2} "

    if not isinstance(text, str):
        print("Passed value must be a string")
        return None

    next_entry = re.search(regex, text)
    while next_entry is not None:
        yield float(next_entry.group(0))
        text = text[next_entry.end():] # Cutting off part that we already found
        next_entry = re.search(regex, text)

    return None

def sum_profit(text: str, func: Callable):
    total_sum = 0.0
    next_entry = func(text) # Creating generator for target text

    for number in next_entry: # Iterating through all entries
        total_sum += number

    return total_sum

def main():
    text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."
    total_income = sum_profit(text, generator_numbers)
    print(f"Загальний дохід: {total_income}")

    total_income = sum_profit("", generator_numbers)
    print(f"Загальний дохід приклад 2: {total_income}")
    total_income = sum_profit("100.00 500.00", generator_numbers)
    print(f"Загальний дохід приклад 3: {total_income}")
    total_income = sum_profit("100,00 500.00", generator_numbers)
    print(f"Загальний дохід приклад 3: {total_income}")
    total_income = sum_profit(" 100.00  500.00 ", generator_numbers)
    print(f"Загальний дохід приклад 3: {total_income}")

if __name__ == '__main__':
    main()