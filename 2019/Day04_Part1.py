start = 256310
end = 732736

def meets_conditions(x):
    # It is a six-digit number.
    # The value is within the range given in your puzzle input.
    # Two adjacent digits are the same (like 22 in 122345).
    # Going from left to right, the digits never decrease; they only ever
    # increase or stay the same (like 111123 or 135679).
    digits = [int(i) for i in str(x)]
    adjacent_same = False
    for i in range(len(digits) - 1):
        if digits[i] == digits[i + 1]:
            adjacent_same = True
            break
    not_decreasing = digits == sorted(digits)
    return adjacent_same and not_decreasing

print(len(list(filter(meets_conditions, range(start, end + 1)))))