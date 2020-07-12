# There are three types of edits that can be performed on strings:
# insert a character, remove a character, or replace a character.
# Given two strings, write a function to check if they are one edit (or zero edits) away.
# EXAMPLE
# pale, ple -> true
# pales, pale -> true
# pale, bale -> true
# pale, bake -> false


def is_one_edit_away(s1, s2):
    if s1 == s2:
        return True
    if abs(len(s1) - len(s2)) > 1:
        return False

    edit_count = 0
    i = j = 0

    while i < len(s1) and j < len(s2):
        if s1[i] != s2[j]:
            if edit_count == 1:
                return False

            if len(s1) > len(s2):
                i += 1
            elif len(s2) > len(s1):
                j += 1
            else:
                i += 1
                j += 1
            edit_count += 1

        else:
            i += 1
            j += 1

    if i < len(s1) and j < len(s2):
        i += 1
        j += 1

    return edit_count == 1


def main():
    print(is_one_edit_away("ales", "pale"))
    print(is_one_edit_away("pale", "ple"))
    print(is_one_edit_away("pale", "bake"))
    print(is_one_edit_away("label", "babel"))


if __name__ == "__main__":
    main()
