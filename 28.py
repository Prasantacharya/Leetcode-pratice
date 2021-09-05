def strStr(haystack, needle):
    for character in range(len(haystack)):
        if (haystack[character: character + len(needle)] == needle):
            return character
    return -1

print(strStr("hello", "ll"))
