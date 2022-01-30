# Problem 1. TODO: @teddy-walsh


# Problem 2. TODO: @teddy-walsh


# Problem 3.
# An 8-digit password is required to have exactly three 0’s. The other 5 digits can be any number 1-7,
# but numbers 1-7 may not be repeated. Write a program that lists the first 100 passwords
# and counts all the possible outcomes.
from typing import List


def count_passwords(num_of_digits: int = 8, possible_value: int = 7) -> int:
    total: int = 0
    slots = possible_value + 1
    z_count = 0
    # iterate through
    cur_zero_digits: List[int] = [0]*3
    cur_digits: List[int] = [0]*5
    # skip over previously chosen number because we are looking at combinations and order doesn't matter.
    for z_1 in range(0, num_of_digits):
        cur_zero_digits[0] =  z_1
        for z_2 in range(z_1 + 1, num_of_digits):
            cur_zero_digits[1] = z_2
            for z_3 in range(z_2 + 1, num_of_digits):
                cur_zero_digits[2] = z_3
                # check for duplicates, because sets aren't allowed to contain duplicates.
                if len(cur_zero_digits) != len(set(cur_zero_digits)):
                    # skip this one
                    continue
                for d_1 in range(1, slots):
                    cur_digits[0] = d_1
                    for d_2 in range(1, slots):
                        cur_digits[1] = d_2
                        for d_3 in range(1, slots):
                            cur_digits[2] = d_3
                            for d_4 in range(1, slots):
                                cur_digits[3] = d_4
                                for d_5 in range(1, slots):
                                    cur_digits[4] = d_5
                                    # check for duplicates, because sets aren't allowed to contain duplicates.
                                    if len(cur_digits) != len(set(cur_digits)):
                                        # skip this iteration
                                        continue
                                    total += 1
                                    value: List[int] = [d_1, d_2, d_3, d_4, d_5]
                                    value.insert(z_1, 0)
                                    value.insert(z_2, 0)
                                    value.insert(z_3, 0)
                                    if total <= 100:
                                        print(value)
    return total


# Problem 4. TODO: @the-mann


if __name__ == "__main__":
    print(count_passwords())
