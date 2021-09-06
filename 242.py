class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        lookup = {}
        for i in range(len(s)):
            if s[i] not in lookup:
                lookup[s[i]] = 0
            if t[i] not in lookup:
                lookup[t[i]] = 0
            lookup[s[i]] += 1
            lookup[t[i]] -= 1
        
        for letter in lookup:
            if lookup[letter] != 0:
                return False
        return True
