# Assume you have a method isSubstring which checks if one word is a substring of another. Given two strings, sl and s2,
# write code to check if s2 is a rotation of s1 using only one call to isSubstring
# (e.g.,"waterbottle" is a rotation of "erbottlewat").


def is_rotation(s1, s2):
    # first: check if the 2 strings are of equal length
    # second: check to see if the non-rotated string is a substring of the double-string of the rotated string
    return len(s1) == len(s2) and s1 in (s2 + s2)


def main():
    print(is_rotation("waterbottle", "erbottlewat"))
    print(is_rotation("label", "ellab"))


if __name__ == "__main__":
    main()
