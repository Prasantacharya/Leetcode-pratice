class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        lower = 0
        upper = 0
        lookup = set()
        longest = 0
        while upper < len(s):
            if s[upper] not in lookup:
                lookup.add(s[upper])
                upper += 1;
                longest = max(longest, len(lookup))
            else:
                lookup.discard( s[lower] )
                # lookup.remove(s[lower])
                lower += 1
        return longest
