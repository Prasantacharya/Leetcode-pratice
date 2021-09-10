class Solution:
    def longestPalindrome(self, s: str) -> str:
        output = ""
        longest = 0
        def subString(left, right, string):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                if (right - left + 1) > len(string):
                    string = s[left:right + 1]
                left -= 1
                right += 1
            return string
        for i in range(len(s)):
            output = subString(i, i, output)
            output = subString(i, i + 1, output)
        return output
