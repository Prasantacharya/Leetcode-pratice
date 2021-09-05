class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        lookup = {"{": "}", "(":")", "[":"]"}
        for character in s:
            if character in ("{", "(", "["):
                stack.append(character)
            elif character in ("}", ")", "]") and len(stack) > 0 and stack[-1] in lookup and lookup[stack[-1]] == character:
                stack.pop()
            else:
                return False
        return (len(stack) == 0)
        
