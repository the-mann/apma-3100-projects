# Problem 1. TODO: @teddy-walsh


# Problem 2. TODO: @teddy-walsh


# Problem 3.
# An 8-digit password is required to have exactly three 0’s. The other 5 digits can be any number 1-7,
# but numbers 1-7 may not be repeated. Write a program that lists the first 100 passwords
# and counts all the possible outcomes.
from functools import reduce
from typing import List, Dict, Union


def count_passwords(num_of_digits: int = 8, possible_value: int = 7) -> int:
    total: int = 0
    slots = possible_value + 1
    z_count = 0
    # iterate through
    cur_zero_digits: List[int] = [0] * 3
    cur_digits: List[int] = [0] * 5
    # skip over previously chosen number because we are looking at combinations and order doesn't matter.
    for z_1 in range(0, num_of_digits):
        cur_zero_digits[0] = z_1
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
                                        print(reduce(lambda a, b: str(a) + str(b), value))
    return total


# Problem 4. A 5-letter password is to be constructed from the following letters: A, B, C, D, and E and the password
# must contain exactly 3 of the letters. (Obviously at least one of them will need to be used more than once to
# create a 5-letter password.)

# Because the instructions for Problem 4 never said anything about points being deducted for using a collection based
# solution, I generate all the passwords and only filter based off the exactly 3 distinct characters requirement,
# which is reused through all 3 parts of Problem 4.
def generate_all_passwords() -> List[Dict[str, Union[str, int]]]:
    ret: List[Dict[str, Union[str, int]]] = []
    letters = ['A', 'B', 'C', 'D', 'E']
    # iterate through all permutations of passwords
    for a in letters:
        for b in letters:
            for c in letters:
                for d in letters:
                    for e in letters:
                        # construct the string from the different permutations of the letters.
                        pwd: str = f"{a}{b}{c}{d}{e}"
                        # Create a dictionary that has a mapping of the characters to the count of the characters
                        # in the password. This will be used in other filters.
                        counts: Dict[str, Union[int, str]] = {}
                        # loop through the characters in the string
                        for i in pwd:
                            # if this string isn't in the counts dictionary, then add it to the dictionary and set it
                            # to 1. otherwise, increment by 1.
                            if i in counts:
                                counts[i] += 1
                            else:
                                counts[i] = 1
                        # only return a password if there are exactly 3 distinct characters. sets aren't allowed to have
                        # duplicate values, so when we check set(pwd), it will deduplicate the string's characters.
                        if len(counts.keys()) == 3:
                            # Store word in counts dictionary for later use
                            counts['word'] = pwd
                            # add to array to later return, and go to next iteration
                            ret.append(counts)
    return ret


# 2 A's, 2 B's, 1 C
def count_4_a(counts: List[Dict[str, int]]) -> int:
    ret: int = 0
    # loop through all of the words that made it through the first round of filtration in generate_all_passwords()
    for c in counts:
        # if A, B, and C are in the dictionary, and if the counts of them are their respective correct counts,
        # then increment the counter by 1.
        if "A" in c.keys() and "B" in c.keys() and "C" in c.keys() and c["A"] == 2 and c["B"] == 2 and c["C"] == 1:
            ret += 1
    return ret


#  Suppose A,B, and C are the letters selected and there are no other restrictions.
#  How many passwords exist in this scenario?
def count_4_b(counts: List[Dict[str, int]]) -> int:
    ret: int = 0
    # loop through all the words that made it through the first round of filtration in generate_all_passwords()
    for c in counts:
        # If A, B, and C are selected:
        if "A" in c.keys() and "B" in c.keys() and "C" in c.keys():
            ret += 1
    return ret


# Now suppose we don’t put any restrictions on the letters chosen. (It could be A,B, and C, or it could be A, C, and D,
# or it could be B, D, and E, etc.) How many different passwords exist in this scenario?
def count_4_c(counts: List[Dict[str, int]]) -> int:
    # we already matched the filter with our original filter in generate_all_passwords(), so return the length.
    return len(counts)


if __name__ == "__main__":
    print(f"The answer to 3.b is {count_passwords()}")
    pwds = generate_all_passwords()
    print(f"The answer to 4.a = {count_4_a(generate_all_passwords())}")
    print(f"The answer to 4.b = {count_4_b(pwds)}")
    print(f"The answer to 4.c = {count_4_c(pwds)}")
