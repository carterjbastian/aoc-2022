from lib.helpers import log, get_strings_by_lines

digit_map = {
    '=': -2,
    '-': -1,
    '0': 0,
    '1': 1,
    '2': 2,
}


def to_decimal(snafu):
    exponent = 0
    total = 0
    for digit in reversed(snafu):
        place_val = 5 ** exponent
        total += (digit_map[digit] * place_val)
        exponent += 1

    return total


def to_snafu(decimal):
    # First convert the number to base 5
    base_5 = []
    while decimal > 0:
        base_5 += [decimal % 5]
        decimal //= 5

    # Convert decimal to snafu
    carry = 0
    snafu = []
    for digit in base_5:
        val = digit + carry
        if val == 0:
            snafu += ['0']
            carry = 0
        if val == 1:
            snafu += ['1']
            carry = 0
        if val == 2:
            snafu += ['2']
            carry = 0
        if val == 3:
            snafu += ['=']
            carry = 1
        if val == 4:
            snafu += ['-']
            carry = 1
        if val == 5:
            snafu += ['0']
            carry = 1
        if val == 6:
            snafu += ['1']
            carry = 1
        if val == 7:
            snafu += ['2']
            carry = 1

    return ''.join(reversed(snafu))


def part_1():
    decimal_vals = []
    for snafu in get_strings_by_lines('25.txt'):
        log(to_decimal(snafu))
        decimal_vals += [to_decimal(snafu)]

    snafu_val = ""
    for val in decimal_vals:
        snafu = to_snafu(val)
        log(f"Decimal {val} to snafu {snafu}")

    return to_snafu(sum(decimal_vals))
