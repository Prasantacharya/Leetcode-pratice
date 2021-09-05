class Solution:
    def countBits(self, n: int) -> List[int]:
        output = []
        for i in range(n + 1):
            ones = 0
            while i > 0:
                ones += i & 1
                i = i >> 1
            output.append(ones)
        return output
