class Solution:
    def reverseBits(self, n: int) -> int:
        output = 0
        for _ in range(31):
            output |= n & 1
            n >>= 1
            output <<= 1
        output |= n & 1
        return output
