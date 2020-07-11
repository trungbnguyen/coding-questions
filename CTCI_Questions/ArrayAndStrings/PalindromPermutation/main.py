# Given a string, write a function to check if it is a permutation of a palindrome.
# A palindrome is a word or phrase that is the same forwards and backwards.
# A permutation is a rearrangement of letters. The palindrome does not need to be limited to just dictionary words.
# EXAMPLE
# Input: Tact Coa
# Output: True (permutations: "taco cat", "atco cta", etc.)


# def merge_sort(l1):
#     if len(l1) <= 1:
#         return l1
#
#     mid = len(l1) // 2
#     left = l1[:mid]
#     right = l1[mid:]
#
#     merge_sort(left)
#     merge_sort(right)
#
#     i = j = k = 0
#
#     while i < len(left) and j < len(right):
#         if left[i] < right[j]:
#             l1[k] = left[i]
#             i += 1
#         else:
#             l1[k] = right[j]
#             j += 1
#     k += 1
#
#     while i < len(left):
#         l1[k] = left[i]
#         i += 1
#         k += 1
#     while j < len(right):
#         l1[k] = right[j]
#         j += 1
#         k += 1
#
#     return l1


def is_permutation_of_palindrome(st):
    if len(st) <= 2:
        return True

    # Find the number of characters with odd occurrences
    def find_odd_occurrences(s):
        count = 0
        d = dict()
        for i in range(len(s)):
            d[s[i]] = d.get(s[i], 0) + 1

        for i in d:
            if d[i] % 2 != 0:
                count += 1
        return count

    st = st.replace(' ', '')
    st = st.lower()
    l1 = list(st)
    odd_count = find_odd_occurrences(l1)

    if odd_count > 1:
        return False
    else:
        return True


def main():
    print(is_permutation_of_palindrome("Tact Coa"))
    print(is_permutation_of_palindrome("gee go"))
    print(is_permutation_of_palindrome("gee k"))


if __name__ == "__main__":
    main()
