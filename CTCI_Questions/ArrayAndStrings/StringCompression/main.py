# Implement a method to perform basic string compression using the counts of repeated characters.
# For example, the string aabcccccaaa would become a2b1c5a3. If the "compressed" string would not
# become smaller than the original string, your method should return the original string.
# You can assume the string has only uppercase and lowercase letters (a - z).


def string_compression(s):
    if len(s) < 2:
        return s

    compressed = ""
    count = 1
    compressed += s[0]

    for i in range(len(s) - 1):
        if s[i] == s[i + 1]:
            count += 1
        else:
            if count >= 1:
                compressed += str(count)
            compressed += s[i + 1]
            count = 1
    if count >= 1:
        compressed += str(count)

    if len(compressed) >= len(s):
        return s
    return compressed


def main():
    print(string_compression("aabcccccaaa"))
    print(string_compression("abc"))
    print(string_compression("mississippi"))


if __name__ == "__main__":
    main()
