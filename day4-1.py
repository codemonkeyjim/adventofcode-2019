#!/usr/bin/env python

START_PIN = 136760
END_PIN = 595730
PIN_LEN = len(str(END_PIN))


def meets_rules(pin: str) -> bool:
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


if __name__ == "__main__":
    all_pins = [str(pin).zfill(PIN_LEN) for pin in range(START_PIN, END_PIN + 1)]
    candidates = list(filter(meets_rules, all_pins))
    print(candidates)
    print(len(candidates))
