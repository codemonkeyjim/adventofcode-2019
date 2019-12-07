#!/usr/bin/env python

START_PIN = 136760
END_PIN = 595730
PIN_LEN = len(str(END_PIN))


def part_1_rules(pin: str) -> bool:
    digits = str(pin)
    prev_digit = int(digits[0])
    doubles = 0
    for str_digit in digits[1:]:
        digit = int(str_digit)
        if digit < prev_digit:
            return False
        if digit == prev_digit:
            doubles += 1
        prev_digit = digit
    return doubles >= 1


def part_2_rules(pin: str) -> bool:
    digits = str(pin)
    has_double = False
    consecutive = 1
    prev_digit = int(digits[0])
    for str_digit in digits[1:]:
        digit = int(str_digit)
        if digit == prev_digit:
            consecutive += 1
        else:
            has_double = has_double or consecutive == 2
            consecutive = 1
        prev_digit = digit
    return has_double or consecutive == 2


if __name__ == "__main__":
    all_pins = [str(pin).zfill(PIN_LEN) for pin in range(START_PIN, END_PIN + 1)]
    part_1_candidates = list(filter(part_1_rules, all_pins))
    print(len(part_1_candidates))
    part_2_candidates = list(filter(part_2_rules, part_1_candidates))
    print(len(part_2_candidates))
    # for test_pin in ['112233', '123444', '111122']:
    #     print(f'{test_pin}: {part_1_rules(test_pin) and part_2_rules(test_pin)}')
