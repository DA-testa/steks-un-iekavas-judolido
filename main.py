# python3

from collections import namedtuple

Bracket = namedtuple("Bracket", ["char", "position"])


def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]


def find_mismatch(text):
    opening_brackets_stack = []
    for i, next in enumerate(text):
        if next in "([{":
            opening_brackets_stack.append(Bracket(next, i+1))
        if next in ")]}":
                        if not opening_brackets_stack:  # If it's a closing bracket, pop the top element from the stack
                return i+1                              # Return index of the first unmatched closing bracket
            pirm = opening_brackets_stack.pop()
            if not are_matching(pirm.char, next):
                return i+1                              # Return index of the first unmatched closing bracket
    if opening_brackets_stack:
        return opening_brackets_stack[0].position       # Return index of the first unmatched opening bracket
    return "Success"
                                                        # Process closing bracket, write your code here


def main():
    text = input()
    mismatch = find_mismatch(text)
    # Printing answer, write your code here


if __name__ == "__main__":
    main()
