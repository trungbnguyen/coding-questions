"""
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Note that an empty string is also considered valid.
"""


def is_valid_parentheses(s):
    """
    Use a stack and as we iterate through the string, if the value at in index i in the dictionary
    does not match its key, which is pop from the stack, then the string is invalid. Otherwise, the stack becomes
    empty, then the string is valid because all the values at index i match their key in the dictionary.
    :param s: input string
    :return: True if the string is valid, False otherwise
    """
    parentheses_d = {')': '(', '}': '{', ']': '['}

    if s == "":
        return True
    elif len(s) % 2 != 0:
        return False
    stack = []
    for i in s:
        if i in parentheses_d.values():
            stack.append(i)
        elif i in parentheses_d.keys():
            if stack == [] or parentheses_d[i] != stack.pop():
                return False
        else:
            return False
    return len(stack) == 0


def main():
    # print(is_valid_parentheses("{}{}(])("))
    # print(is_valid_parentheses("()[]{}"))
    print(is_valid_parentheses("([)]"))
    # print(is_valid_parentheses("()[]{}"))
    is_valid_parentheses("{[]}")


if __name__ == "__main__":
    main()
