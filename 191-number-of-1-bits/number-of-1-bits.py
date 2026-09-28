class Solution:
    def hammingWeight(self, n: int) -> int:
        start = 31
        count = 0
        while start >= 0:
            if n >= 2**start:
                n -= 2**start
                count += 1
            start -= 1
            if n == 0:
                break
        return count