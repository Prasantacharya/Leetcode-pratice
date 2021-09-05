class Solution:
    def consecutiveNumbersSum(self, n: int) -> int:
        start = 3
        num = 2
        count = 1
        while n >= start:
            if (n - start) % num == 0:
                count += 1
            num += 1
            start += num
        return count
