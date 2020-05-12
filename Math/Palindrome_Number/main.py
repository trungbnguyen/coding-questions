def is_palindrome(x):
    """
    Determine whether an integer is a palindrome. An integer is a palindrome when it reads the same backward as forward.
    :parameter x: input integer
    :return: True if it's a palindrome, False otherwise
    """
    if x < 0:
        return False

    original = x
    reverse = 0
    while x > 0:
        last_digit = x % 10
        reverse = reverse * 10 + last_digit
        x //= 10

    return reverse == original


def main():
    print(is_palindrome(121))
    print(is_palindrome(-121))
    print(is_palindrome(10))


if __name__ == "__main__":
    main()
