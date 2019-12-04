start = 256310
end = 732736

def meets_conditions(x):
    digits = [int(i) for i in str(x)]
    match_next = []
    distinct = False
    for i in range(len(digits) - 1):
        match_next.append(digits[i] == digits[i + 1])
    for i in range(len(match_next)):
        if match_next[i]:
            if i == 0:
                distinct = True and not match_next[i + 1]
            elif i == len(match_next) - 1:
                distinct = True and not match_next[i - 1]
            else:
                distinct = (True and not match_next[i - 1]
                                 and not match_next[i + 1])
        if distinct:
            break
    not_decreasing = digits == sorted(digits)
    return distinct and not_decreasing

assert meets_conditions(112233) == True
assert meets_conditions(123444) == False
assert meets_conditions(124444) == False
assert meets_conditions(111122) == True
print(len(list(filter(meets_conditions, range(start, end + 1)))))